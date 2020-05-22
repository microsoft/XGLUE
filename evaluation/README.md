# Evaluation
We will use following command to evaluate your model's performance on test dataset: 
```
python xglue_evaluate.py --prediction_dir <prediction_files_folder> --ground_truth_dir <ground_truth_dir> --tasks NER,POS,NC,MLQA,XNLI,PAWSX,QADSM,WPR,QAM,QG,NTG [--split test] 
```
Before submission, you could test your output format on dev dataset with following command:
```
python xglue_evaluate.py --prediction_dir <prediction_files_folder> --ground_truth_dir <ground_truth_dir> --tasks NER,POS,NC,MLQA,XNLI,PAWSX,QADSM,WPR,QAM,QG,NTG --split dev 
```

We provide the output of Unicoder as [dev example](Unicoder_prediction_on_XGLUE_dev) and [test example](Unicoder_prediction_on_XGLUE_test).

The evaluation files has several dependencies:
```
numpy
sklearn
seqeval
sacrebleu
```

# prediction file format
For all the tasks except MLQA and PAWS-X, the line number of each prediction file should be same as the input file. The i-th line of input corresponding to i-th line of output.

PAWS-X's input file has one additional header. 

MLQA uses JSON format.

Detailed information for each task:

    QAM:
		QAM/*.prediction:		predicted label
		(Label should be in [0, 1])

	QADSM:
		QADSM/*.prediction:		predicted label
		(Label should be in ["Good", "Bad"])

	WPR:
		WPR/*.prediction:		predicted label
		(Label should be in [0, 1, 2, 3, 4], the meaning of every rating is presented by the dictionary: {"perfect":"4", "excellent":"3", "good":"2", "fair":"1", "bad":"0"})

	NC:
		NC/*.prediction:			predicted label
		(Label should be in ["foodanddrink", "sports", "news", "entertainment", "health", "video", "finance", "travel", "lifestyle", "autos"])

	QG:
		QG/*.prediction:		predicted question

	NTG:
		NTG/*.prediction:  	predicted news title

	XNLI:
		XNLI/*.prediction:		predicted label
		(Label should be in ["neutral", "contradiction", "entailment"])

	NER:
		NER/*.prediction:		predicted label of each word
		(Label should be in ["B-LOC", "B-MISC", "B-ORG", "B-PER", "I-LOC", "I-MISC", "I-ORG", "I-PER", "O"])

	POS:
		POS/*.prediction:		predicted label of each word
		(Label should be in ["ADJ", "ADP", "ADV", "AUX", "CCONJ", "DET", "INTJ", "NOUN", "NUM", "PART", "PRON", "PROPN", "PUNCT", "SCONJ", "SYM", "VERB", "X"])

	PAWS-X:
		PAWSX/*.prediction:		predicted label
		(Label should be in [0, 1])

	MLQA:
		MLQA/*.prediction:		{"qas_id1": "answer text 1", "qas_id2": "answer text 2"}