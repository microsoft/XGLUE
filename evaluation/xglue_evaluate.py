import argparse
import sacrebleu
import os
import sys
import string
from collections import Counter
import json
import re
import numpy as np
import copy
import unicodedata
from mlqa_evaluation_v1 import evaluate as mlqa_evaluate
from seqeval.metrics import f1_score, precision_score, recall_score, accuracy_score
from sklearn.metrics import ndcg_score

parser = argparse.ArgumentParser()
parser.add_argument(
        "--prediction_dir",
        default=None,
        type=str,
        required=True,
        help="The prediction data dir. Should contain the .tsv files (or other data files) for the task.",
)

parser.add_argument(
        "--ground_truth_dir",
        default=None,
        type=str,
        required=True,
        help="The ground truth data dir. Should contain the .tsv files (or other data files) for the task.",
)

parser.add_argument(
        "--tasks",
        default=None,
        type=str,
        required=True,
        help="The task name. Should be one or several of NER, POS, NC, MLQA, XNLI, PAWSX, QADSM, WPR, QAM, QG, NTG",
)

parser.add_argument(
        "--split",
        default="test",
        type=str,
        required=False,
        help="The split name. Should be one of test dev",
)


args = parser.parse_args()


task2lg = {
"NER" : "de en es nl",
"POS" : "pl ar ru bg de el en es fr hi it nl pt th tr ur vi zh",  # pl  
"NC" : "de en es fr ru", 
"MLQA" : "ar de en es hi vi zh", 
"XNLI" : "ar bg de el en es fr hi ru sw th tr ur vi zh",
"PAWSX" : "de en es fr",
"QADSM" : "de en fr", 
"WPR" : "de en es fr it pt zh", 
"QAM" : "de en fr",
"QG" : "de en es fr it pt",
"NTG" : "de en es fr ru"
}



def simple_accuracy(preds, labels):
    return (preds == labels).mean()

def simple_ndcg(preds, labels, guids):
    ndcgs = []
    query2content = {}
    for guid, pred, label in zip(guids, preds, labels):
        query = guid
        if not query in query2content:
            query2content[query] = [[float(pred)], [float(label)]]
        else:
            query2content[query][0].append(float(pred))
            query2content[query][1].append(float(label))

    for key in query2content.keys():
        if len(query2content[key][1]) < 2 or len(query2content[key][0]) < 2:
            continue
        ndcgs.append(ndcg_score(np.asarray([query2content[key][1]]), np.asarray([query2content[key][0]])))
    return np.array(ndcgs).mean()

   

def load_mlqa_data(task, lg):
    dataset_file = os.path.join(args.ground_truth_dir, "{0}/MLQA_V1/{1}/{1}-context-{2}-question-{2}.json".format(task, args.split, lg))
    pred_file = os.path.join(args.prediction_dir, "{0}/{1}.prediction".format(task, lg))
    dataset = json.load(open(dataset_file))
    preds = json.load(open(pred_file))
    return dataset, preds

def load_pawsx_data(task, lg):
    pred_file = os.path.join(args.prediction_dir, "{0}/{1}.prediction".format(task, lg))
    label_file = os.path.join(args.ground_truth_dir, "{0}/{1}/{2}_2k.tsv".format(task, lg, args.split))
    preds = []
    labels = []
    for item in open(pred_file):
        preds.append(item.strip())
    count = 0
    for item in open(label_file):
        if count == 0:
            count += 1
            continue
        if not len(item.strip()) == 0:
            labels.append(item.split("\t")[-1].strip())
    return np.array(labels), np.array(preds) 

def load_xnli_data(task, lg):
    pred_file = os.path.join(args.prediction_dir, "{0}/{1}.prediction".format(task, lg))
    label_file = os.path.join(args.ground_truth_dir, "{0}/{1}.{2}".format(task, lg, args.split))
    labels = []
    preds = []
    for item in open(pred_file):
        preds.append(item.strip())
    count = 0
    for line in open(label_file):
        label = line.split("\t")[-1]
        labels.append(label.strip())
    return np.array(preds), np.array(labels)

def load_ner_pos_data(task,lg):
    pred_file = os.path.join(args.prediction_dir, "{0}/{1}.prediction".format(task, lg))
    label_file = os.path.join(args.ground_truth_dir, "{0}/{1}.{2}".format(task, lg, args.split))

    preds, labels = [], []
    pred = []
    label = []
    for item in open(pred_file):
        if len(item.strip()) == 0 and len(pred) > 0:
            preds.append(pred)
            pred = []
            continue  
        pred.append(item.strip())

    if len(pred) > 0:
        preds.append(pred)

    for item in open(label_file):
        if not (len(item.strip()) == 0 or item.startswith("-DOCSTART-")):
            label.append(item.split()[-1].strip())
        elif len(label) > 0:
            labels.append(label)
            label = []
    if len(label) > 0:
        labels.append(label)

    for i in range(len(labels)):
        while len(labels[i]) > len(preds[i]):
            preds[i].append("O")
    return np.array(preds), np.array(labels)

def load_qg_ntg_data(task, lg):
    pred_file = os.path.join(args.prediction_dir, "{0}/{1}.prediction".format(task, lg))
    label_file = os.path.join(args.ground_truth_dir, "{0}/xglue.{1}.{2}.tgt.{3}".format(task, task.lower(), lg, args.split))

    preds, labels = [], []
    last_query = ""
    for item in open(pred_file, encoding='utf8'):
        preds.append(item.strip())
    
    for item in open(label_file, encoding='utf8'):
        last_query = item.split("\t")[0]
        labels.append(item.split("\t")[-1].strip())

    return np.array(preds), np.array(labels)
 

def load_data(task, lg):
    pred_file = os.path.join(args.prediction_dir, "{0}/{1}.prediction".format(task, lg))
    label_file = os.path.join(args.ground_truth_dir, "{0}/xglue.{1}.{2}.{3}".format(task, task.lower(), lg, args.split))
    preds, labels, guids = [], [], []
    last_query = ""
    for item in open(pred_file):        
        preds.append(item.strip())
    
    guid = 0
    for item in open(label_file):
        if task == "WPR" and (not item.split("\t")[0] == last_query) and len(last_query) > 0:
            guid += 1
        last_query = item.split("\t")[0]
        labels.append(item.split("\t")[-1].strip())
        guids.append(guid)

    return np.array(preds), np.array(labels), np.array(guids)

def get_score_by_task(task):
    results = {}
    for lg in task2lg[task].split():
        preds = []
        labels = []
        guid = 0
        guids = []
        if task == "MLQA":
            datasets, preds = load_mlqa_data(task, lg)
        elif task in ["NC", "QADSM", "QAM", "WPR"]:
            preds, labels, guids = load_data(task, lg)
        elif task in ["QG", "NTG"]:
            preds, labels = load_qg_ntg_data(task, lg)
        elif task in ["NER", "POS"]:
            preds, labels  = load_ner_pos_data(task, lg)
        elif task == "XNLI":
            labels, preds = load_xnli_data(task, lg)
        elif task == "PAWSX":
            labels, preds = load_pawsx_data(task, lg)   

        if task == "MLQA":
            results[lg] = mlqa_evaluate(datasets["data"], preds, lg)["f1"]/100 #Normalize
        elif task == "NER":
            results[lg] = f1_score(labels, preds)
        elif task == "POS":
            results[lg] = precision_score(labels, preds)
        elif task in ["NC", "XNLI", "PAWSX", "QADSM", "QAM"]:
            results[lg] = simple_accuracy(preds, labels)
        elif task == "WPR":
            results[lg] = simple_ndcg(preds, labels, guids)
        elif task == "QG" or task == "NTG":
            results[lg] = sacrebleu.corpus_bleu(preds, [labels], lowercase=True).score/100 #Normalize
    avg = 0
    count = 0
    for key in results.keys():
        avg += results[key]
        count += 1
    avg /= count
    results["avg"] = avg
    return results

task2result = {}
averages = []
for task in args.tasks.split(","):
    task2result[task] = get_score_by_task(task)
    print(task)
    print(task2result[task])
    averages.append(task2result[task]["avg"])
print("Average across all tasks:{}".format(np.mean(averages))) 
