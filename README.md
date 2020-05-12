# XGLUE: 
[**Tasks**](#tasks-and-languages) |
[**Data**](#get-the-data) |
[**Website**](https://microsoft.github.io/msmarco/) |
[**Paper**](https://arxiv.org/abs/2004.01401)

This repository contains information about XGLUE, baseline systems, and evaluation methodology. 

## Introduction
This repository contains information about the large-scale cross-lingual evaluation benchmark XGLUE. XLGUE consists of 11 tasks which cover both natural language understanding and natural language generation across a broad array of languages. This repository focuses on data usage, evaluation, and introduces a set of publicly reproducable baselines.  

## Tasks and Languages
The 11 tasks in XGLUE can be categorized into 3 groups: single-input understanding,  pair-input understanding, and generation. For each task training data is only availible for english while evaluation is performed on task specific variety of languages.

### Single-Input Understanding
#### NER
Named Entity Resolution(NER) is a combination of two existing NER tasks which covers 4 languages: English, German, Spanish, and Dutch. The task covers 4 types of named entities: person, location, organiation and miscellaneous. F1 is used as this tasks evaluation metric.
#### POS Tagging
Part of speech(POS) taggig is a subset of the Universal Dependen-cies (UD) Treebanks (v2.5) which cover 18 languages. Accuracy (ACC) of the predicted POS tags is this tasks evaluation metric.
#### News Classification
News classification(NC) is category prediction for a newsarticle. The task covers 10 different news categories and 5 languages: English, Spanish, French, German, and Russian. Accuracy (ACC) of the multiclass classification is this tasks evaluation metric.
 
### Pair-input Understanding 
#### MLQA
Multilingual Question answering(MLQA) is a multilingual machine reading comprehension task,which covers 7 langauges:English,Arabic,German,Span-ish,Hindi,Vietnamese, and Chinese.  F1 score of the predicted answers is this tasks evaluation metric.
#### XNLI
Cross Linugual Natural Language Inference(XNLI) is reused from the original dataset.
#### PAWS-X
Paraphrase indentifaction(PAWS-X) is built on the existing dataset where we select 4 languages to evaluate on:English,Spanish,French and German. Accuracy (ACC) of the binary task is this tasks evaluation metric.
#### Query-Ads Matching(QADSM)
Query-Ads Matching(QADSM) is formulated on finding the most relevant ad given a users issued query. Data is collected from a commercial search engine, Bing, and covers 3 languages:English, French and German. Each labeled in-stance is a 4-tuple:<query, ad title, ad description,label>.  Accuracy (ACC) of the binary task is this tasks evaluation metric.c
#### Web Page Ranking(WPR)
Web Page Ranking(WPR) is formulated around finding the most relevant webpage given a users issued query. Data is collected from a commercial search engine, Bing, and covers 6 languages: English, German, French, Italian, Portugal and Chinese. Each labeled in-stance is a 4-tuple:<query, web page title, web page snippet, label>.  The labels are highly relevance, middle relevance, lowrelevance and not related. Normalize DiscountedCumulative Gain (nDCG) is this tasks evaluation metric.

#### Question Answering Matching(QAM)
Question Anwering Matching(QAM) is formulated on the match of a given users question and an answer. Data is collected from a commercial search engine, Bing, and covers 3 languages: English, French and German. Each labeled instance is a 3-tuple:<question, passage, label>. The label indicates whether the passage is the answer of the question, or not.  Accuracy (ACC) of the binary classification is this tasks evaluation metric.

### Generation Task
#### Question Generation
Question Generation is formulated around the generation of a question for a given passage.  We con-struct this dataset based on a commercial search engine, Bing, and covers 6 languages English, French, German, Spanish, Italian and Portuguese. BLEU-4 score is this tasks evaluation metric.

#### News Title Generation(NTG) 
News Title Generation if formalized around generating a title for a specific new document. This dataset is created by crawling news websites and covers 5 languages: German, English, French, Spanish and Russian. BLEU-4 score is this tasks evaluation metric.

## Get The data
In order to use our dataset please navigate to [MSMARCO](https://microsoft.github.io/msmarco/) and agree to our terms of service. After you do so a download link will be made available.

## Baseline System
This is where we add about our baseline model, how to use, how it was trained, etc. 

## Leaderboard Submission
### Submissions
To submit your predictions for evaluation please create a single folder which contains the 11 sub-folders named after each task(See reference file for an example). Inside each folder, create one candidate file for each language and name the file using the following format: `candidate-{language}.{extension}` where `{language}` is the 2 character language code and `{extension}` is the task specific extension type. Please validate that you have done this correctly by evaluating against the development file. Once that is done <a href='ms-marco@microsoft.com'>email your submission</a>. We will reply with your model performance.  
### Evaluation
To evaluate your models performance we will compare your candidate files with the reference files using the following command. We are keeping our evaluation data held out but we ask all models first evaluate performance on the development portion of the dataset before submiting their candidates for the evaluation dataset. To evaluate your performance please use the following command: 
```
python evaluate.py <candidate_files_folder> <reference_files_folder>
```
## Paper
If you use our benchmark or dataset please cite our paper `\cite{Liang2020XGLUEAN}`.
```
@article{Liang2020XGLUEAN,
  title={XGLUE: A New Benchmark Dataset for Cross-lingual Pre-training, Understanding and Generation},
  author={Yaobo Liang and Nan Duan and Yeyun Gong and Ning Wu and Fenfei Guo and Weizhen Qi and Ming Gong and Linjun Shou and Daxin Jiang and Guihong Cao and Xiaodong Fan and Bruce Zhang and Rahul Agrawal and Edward Cui and Sining Wei and Taroon Bharti and Ying Qiao and Jiun-Hung Chen and Winnie Wu and Shuguang Liu and Fan Yang and Rangan Majumder and Ming Zhou},
  journal={ArXiv},
  year={2020},
  volume={abs/2004.01401}
}
```

Additionally, since our dataset is also built out of exiting baselines please ensure you also cite all the invidicual datasets. 

Example:
We evaluate our model using the XGLUE benchmark `\cite{Liang2020XGLUEAN}` , a language understanding benchmark consiting of Named Entity Resolution(NER) `cite{Sang2003IntroductionTT}` `cite{Sang2002IntroductionTT}` , Part of Speech(POS) Tagging `\cite{11234/1-3105}`, News Classification(NC), Multilingual Question ansering MLQA `\cite{Lewis2019MLQAEC}`, Cross-Lingual Natural Language Inference(XNLI) `\cite{Conneau2018XNLIEC}`, paraphrase identification (PAWS-X) `\cite{Yang2019PAWSXAC}`, Query-Ads Matching(QADSM, Web Page Ranking(WPR), Question Answering Matching(QAM), Question Generation(QG), and News Title Generation (NTG).


Bibtex for datasets used in XGLUE
```
@misc{11234/1-3105,
 title = {Universal Dependencies 2.5},
 author = {Zeman, Daniel and Nivre, Joakim and Abrams, Mitchell and Aepli, No{\"e}mi and Agi{\'c}, {\v Z}eljko and Ahrenberg,
 Lars and Aleksandravi{\v c}i{\=u}t{\.e}, Gabriel{\.e} and Antonsen, Lene and Aplonova, Katya and Aranzabe, Maria Jesus and Arutie, Gashaw and Asahara, Masayuki and Ateyah, Luma and Attia, Mohammed and Atutxa, Aitziber and Augustinus, Liesbeth and Badmaeva, Elena and Ballesteros, Miguel and Banerjee, Esha and Bank, Sebastian and Barbu Mititelu, Verginica and Basmov, Victoria and Batchelor, Colin and Bauer, John and Bellato, Sandra and Bengoetxea, Kepa and Berzak, Yevgeni and Bhat, Irshad Ahmad and Bhat, Riyaz Ahmad and Biagetti, Erica and Bick, Eckhard and Bielinskien{\.e}, Agn{\.e} and Blokland, Rogier and Bobicev, Victoria and Boizou, Lo{\"{\i}}c and Borges V{\"o}lker, Emanuel and B{\"o}rstell, Carl and Bosco, Cristina and Bouma, Gosse and Bowman, Sam and Boyd, Adriane and Brokait{\.e}, Kristina and Burchardt, Aljoscha and Candito, Marie and Caron, Bernard and Caron, Gauthier and Cavalcanti, Tatiana and Cebiro{\u g}lu Eryi{\u g}it, G{\"u}l{\c s}en and Cecchini, Flavio Massimiliano and Celano, Giuseppe G. A. and {\v C}{\'e}pl{\"o}, Slavom{\'{\i}}r and Cetin, Savas and Chalub, Fabricio and Choi, Jinho and Cho, Yongseok and Chun, Jayeol and Cignarella, Alessandra T. and Cinkov{\'a}, Silvie and Collomb, Aur{\'e}lie and {\c C}{\"o}ltekin, {\c C}a{\u g}r{\i} and Connor, Miriam and Courtin, Marine and Davidson, Elizabeth and de Marneffe, Marie-Catherine and de Paiva, Valeria and de Souza, Elvis and Diaz de Ilarraza, Arantza and Dickerson, Carly and Dione, Bamba and Dirix, Peter and Dobrovoljc, Kaja and Dozat, Timothy and Droganova, Kira and Dwivedi, Puneet and Eckhoff, Hanne and Eli, Marhaba and Elkahky, Ali and Ephrem, Binyam and Erina, Olga and Erjavec, Toma{\v z} and Etienne, Aline and Evelyn, Wograine and Farkas, Rich{\'a}rd and Fernandez Alcalde, Hector and Foster, Jennifer and Freitas, Cl{\'a}udia and Fujita, Kazunori and Gajdo{\v s}ov{\'a}, Katar{\'{\i}}na and Galbraith, Daniel and Garcia, Marcos and G{\"a}rdenfors, Moa and Garza, Sebastian and Gerdes, Kim and Ginter, Filip and Goenaga, Iakes and Gojenola, Koldo and G{\"o}k{\i}rmak, Memduh and Goldberg, Yoav and G{\'o}mez Guinovart, Xavier and Gonz{\'a}lez Saavedra,
 Berta and Grici{\=u}t{\.e}, Bernadeta and Grioni,
 Matias and Gr{\=
u}z{\={\i}}tis, Normunds and Guillaume, Bruno and Guillot-Barbance, C{\'e}line and Habash, Nizar and Haji{\v c}, Jan and Haji{\v c} jr., Jan and H{\"a}m{\"a}l{\"a}inen, Mika and H{\`a} M{\~y}, Linh and Han, Na-Rae and Harris, Kim and Haug, Dag and Heinecke, Johannes and Hennig, Felix and Hladk{\'a}, Barbora and Hlav{\'a}{\v c}ov{\'a}, Jaroslava and Hociung, Florinel and Hohle, Petter and Hwang, Jena and Ikeda, Takumi and Ion, Radu and Irimia, Elena and Ishola, {\d O}l{\'a}j{\'{\i}}d{\'e} and Jel{\'{\i}}nek, Tom{\'a}{\v s} and Johannsen, Anders and J{\o}rgensen, Fredrik and Juutinen, Markus and Ka{\c s}{\i}kara, H{\"u}ner and Kaasen, Andre and Kabaeva, Nadezhda and Kahane, Sylvain and Kanayama, Hiroshi and Kanerva, Jenna and Katz, Boris and Kayadelen, Tolga and Kenney, Jessica and Kettnerov{\'a}, V{\'a}clava and Kirchner, Jesse and Klementieva, Elena and K{\"o}hn, Arne and Kopacewicz, Kamil and Kotsyba, Natalia and Kovalevskait{\.e}, Jolanta and Krek, Simon and Kwak, Sookyoung and Laippala, Veronika and Lambertino, Lorenzo and Lam, Lucia and Lando, Tatiana and Larasati, Septina Dian and Lavrentiev, Alexei and Lee, John and L{\^e} H{\`{\^o}}ng, Phương and Lenci, Alessandro and Lertpradit, Saran and Leung, Herman and Li, Cheuk Ying and Li, Josie and Li, Keying and Lim, {KyungTae} and Liovina, Maria and Li, Yuan and Ljube{\v s}i{\'c}, Nikola and Loginova, Olga and Lyashevskaya, Olga and Lynn, Teresa and Macketanz, Vivien and Makazhanov, Aibek and Mandl, Michael and Manning, Christopher and Manurung, Ruli and M{\u a}r{\u a}nduc, C{\u a}t{\u a}lina and Mare{\v c}ek, David and Marheinecke, Katrin and Mart{\'{\i}}nez Alonso, H{\'e}ctor and Martins, Andr{\'e} and Ma{\v s}ek, Jan and Matsumoto, Yuji and {McDonald}, Ryan and {McGuinness}, Sarah and Mendon{\c c}a, Gustavo and Miekka, Niko and Misirpashayeva, Margarita and Missil{\"a}, Anna and Mititelu, C{\u a}t{\u a}lin and Mitrofan, Maria and Miyao, Yusuke and Montemagni, Simonetta and More, Amir and Moreno Romero, Laura and Mori, Keiko Sophie and Morioka, Tomohiko and Mori, Shinsuke and Moro, Shigeki and Mortensen, Bjartur and Moskalevskyi, Bohdan and Muischnek, Kadri and Munro, Robert and Murawaki, Yugo and M{\"u}{\"u}risep, Kaili and Nainwani, Pinkey and Navarro Hor{\~n}iacek, Juan Ignacio and Nedoluzhko,
 Anna and Ne{\v s}pore-B{\=e}rzkalne, Gunta and Nguy{\~{\^e}}n Th{\d i}, Lương and Nguy{\~{\^e}}n Th{\d i} Minh, Huy{\`{\^e}}n and Nikaido, Yoshihiro and Nikolaev, Vitaly and Nitisaroj, Rattima and Nurmi, Hanna and Ojala, Stina and Ojha, Atul Kr. and Ol{\'u}{\`o}kun, Ad{\'e}day{\d o}̀ and Omura, Mai and Osenova, Petya and {\"O}stling, Robert and {\O}vrelid, Lilja and Partanen, Niko and Pascual, Elena and Passarotti, Marco and Patejuk, Agnieszka and Paulino-Passos, Guilherme and Peljak-{\L}api{\'n}ska, Angelika and Peng, Siyao and Perez, Cenel-Augusto and Perrier, Guy and Petrova, Daria and Petrov, Slav and Phelan, Jason and Piitulainen, Jussi and Pirinen, Tommi A and Pitler, Emily and Plank, Barbara and Poibeau, Thierry and Ponomareva, Larisa and Popel, Martin and Pretkalni{\c n}a, Lauma and Pr{\'e}vost, Sophie and Prokopidis, Prokopis and Przepi{\'o}rkowski, Adam and Puolakainen, Tiina and Pyysalo, Sampo and Qi, Peng and R{\"a}{\"a}bis, Andriela and Rademaker, Alexandre and Ramasamy, Loganathan and Rama, Taraka and Ramisch, Carlos and Ravishankar, Vinit and Real, Livy and Reddy, Siva and Rehm, Georg and Riabov, Ivan and Rie{\ss}ler, Michael and Rimkut{\.e}, Erika and Rinaldi, Larissa and Rituma, Laura and Rocha, Luisa and Romanenko, Mykhailo and Rosa, Rudolf and Rovati, Davide and Roșca, Valentin and Rudina, Olga and Rueter, Jack and Sadde, Shoval and Sagot, Beno{\^{\i}}t and Saleh, Shadi and Salomoni, Alessio and Samard{\v z}i{\'c}, Tanja and Samson, Stephanie and Sanguinetti, Manuela and S{\"a}rg,
 Dage and Saul{\={\i}}te, Baiba and Sawanakunanon, Yanin and Schneider, Nathan and Schuster, Sebastian and Seddah, Djam{\'e} and Seeker, Wolfgang and Seraji, Mojgan and Shen, Mo and Shimada, Atsuko and Shirasu, Hiroyuki and Shohibussirri, Muh and Sichinava, Dmitry and Silveira, Aline and Silveira, Natalia and Simi, Maria and Simionescu, Radu and Simk{\'o}, Katalin and {\v S}imkov{\'a}, M{\'a}ria and Simov, Kiril and Smith, Aaron and Soares-Bastos, Isabela and Spadine, Carolyn and Stella, Antonio and Straka, Milan and Strnadov{\'a}, Jana and Suhr, Alane and Sulubacak, Umut and Suzuki, Shingo and Sz{\'a}nt{\'o}, Zsolt and Taji, Dima and Takahashi, Yuta and Tamburini, Fabio and Tanaka, Takaaki and Tellier, Isabelle and Thomas, Guillaume and Torga, Liisi and Trosterud, Trond and Trukhina, Anna and Tsarfaty, Reut and Tyers, Francis and Uematsu, Sumire and Ure{\v s}ov{\'a}, Zde{\v n}ka and Uria, Larraitz and Uszkoreit, Hans and Utka, Andrius and Vajjala, Sowmya and van Niekerk, Daniel and van Noord, Gertjan and Varga, Viktor and Villemonte de la Clergerie, Eric and Vincze, Veronika and Wallin, Lars and Walsh, Abigail and Wang, Jing Xian and Washington, Jonathan North and Wendt, Maximilan and Williams, Seyi and Wir{\'e}n, Mats and Wittern, Christian and Woldemariam, Tsegay and Wong, Tak-sum and Wr{\'o}blewska, Alina and Yako, Mary and Yamazaki, Naoki and Yan, Chunxiao and Yasuoka, Koichi and Yavrumyan, Marat M. and Yu, Zhuoran and {\v Z}abokrtsk{\'y}, Zden{\v e}k and Zeldes, Amir and Zhang, Manying and Zhu, Hanzhi},
 url = {http://hdl.handle.net/11234/1-3105},
 note = {{LINDAT}/{CLARIAH}-{CZ} digital library at the Institute of Formal and Applied Linguistics ({{\'U}FAL}), Faculty of Mathematics and Physics, Charles University},
 copyright = {Licence Universal Dependencies v2.5},
 year = {2019} }
@article{Sang2003IntroductionTT,
  title={Introduction to the CoNLL-2003 Shared Task: Language-Independent Named Entity Recognition},
  author={Erik F. Tjong Kim Sang and Fien De Meulder},
  journal={ArXiv},
  year={2003},
  volume={cs.CL/0306050}
}

@article{Sang2002IntroductionTT,
  title={Introduction to the CoNLL-2002 Shared Task: Language-Independent Named Entity Recognition},
  author={Erik F. Tjong Kim Sang},
  journal={ArXiv},
  year={2002},
  volume={cs.CL/0209010}
}
@inproceedings{Conneau2018XNLIEC,
  title={XNLI: Evaluating Cross-lingual Sentence Representations},
  author={Alexis Conneau and Guillaume Lample and Ruty Rinott and Adina Williams and Samuel R. Bowman and Holger Schwenk and Veselin Stoyanov},
  booktitle={EMNLP},
  year={2018}
}
@article{Lewis2019MLQAEC,
  title={MLQA: Evaluating Cross-lingual Extractive Question Answering},
  author={Patrick Lewis and Barlas Oguz and Ruty Rinott and Sebastian Riedel and Holger Schwenk},
  journal={ArXiv},
  year={2019},
  volume={abs/1910.07475}
}
@article{Yang2019PAWSXAC,
  title={PAWS-X: A Cross-lingual Adversarial Dataset for Paraphrase Identification},
  author={Yinfei Yang and Yuan Zhang and Chris Tar and Jason Baldridge},
  journal={ArXiv},
  year={2019},
  volume={abs/1908.11828}
}
```
# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
