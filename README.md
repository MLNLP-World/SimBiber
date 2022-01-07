# SimBiber: A tool for simplifying bibtex with official info.

<img src="figure/MLNLP.png" alt=" " style="width:60%" />

We often need to simplify the official bib that consists of many information into a shorter version that only maintains necessary information (e.g., author, title, conference/journal name and etc) due to page limitation.

We introduce __SimBiber__, a simple tool in Python to simplify them automatically. Hope it's helpful for you.

We also highly recommend another wonderful tool for you [Rebiber](https://github.com/yuchenlin/rebiber), which is a tool for normalizing bibtex with official info.

## Changelog

- **2021.01.06**
  We fix a few minor bugs and add more categories of conferences. (now support <span style="color:red;"><b>84</b></span> conferences)
- **2021.12.31**
  ~~We build the first version and release it.~~

## Installation

```python
git clone https://github.com/MLNLP-World/Simbiber.git
pip install bibtexparser
```

## Usage（v0.2.0）

```bash 
python SimBiberParser.py --input_path data/bibtex.bib --output_path out/bibtex.bib --config_path config --if_append_output False --cache_num 100
```
| argument | usage|
| ----------- | ----------- |
| `--input_path` | The path to the input bib file that you want to simplify |
| `--output_path` | The path to the output bib file that you want to save. |
| `--config_path` | The path to the mapper config file. The path can be a file directory path, like `config` or a single file path, like `config.json`. <br/> <b>PLEASE ATTENTION:</b> If you want to simplify a huge bib file, you'd better extract external json config file to achieve satisfactory speed. |
| `--if_append_output` | Whether append simplified data to output bib file. |
| `--cache_num` | The number of bib items you want to simplify at once.<br/> <b>PLEASE ATTENTION:</b> If you want to simplify a huge bib file, you'd better change it to achieve satisfactory speed. |


## Example Input and Output
An example simplified output entry with the official information:
```bib
@inproceedings{qin-etal-2019-stack,
    title = "A Stack-Propagation Framework with Token-Level Intent Detection for Spoken Language Understanding",
    author = "Qin, Libo  and
      Che, Wanxiang  and
      Li, Yangming  and
      Wen, Haoyang  and
      Liu, Ting",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing and the 9th International Joint Conference on Natural Language Processing (EMNLP-IJCNLP)",
    month = nov,
    year = "2019",
    address = "Hong Kong, China",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/D19-1214",
    doi = "10.18653/v1/D19-1214",
    pages = "2078--2087",
    abstract = "Intent detection and slot filling are two main tasks for building a spoken language understanding (SLU) system. The two tasks are closely tied and the slots often highly depend on the intent. In this paper, we propose a novel framework for SLU to better incorporate the intent information, which further guiding the slot filling. In our framework, we adopt a joint model with Stack-Propagation which can directly use the intent information as input for slot filling, thus to capture the intent semantic knowledge. In addition, to further alleviate the error propagation, we perform the token-level intent detection for the Stack-Propagation framework. Experiments on two publicly datasets show that our model achieves the state-of-the-art performance and outperforms other previous methods by a large margin. Finally, we use the Bidirectional Encoder Representation from Transformer (BERT) model in our framework, which further boost our performance in SLU task.",
}
```


An example simplified output entry from the official information:
```bib
@inproceedings{qin-etal-2019-stack,
    author = {Qin, Libo  and
     Che, Wanxiang  and
     Li, Yangming  and
     Wen, Haoyang  and
     Liu, Ting},
    booktitle = {Proc. of EMNLP},
    title = {A Stack-Propagation Framework with Token-Level Intent Detection for Spoken Language Understanding},
    year = {2019}
}
```


## Supported Conferences 

The `parserConfig.json` contains a list of converted json files of the mapper between official full name and simplified name.

### AI

| Full Name | Name |
| --- | ----------- |
|Association for the Advance of Artificial Intelligence|AAAI|
|International Joint Conference on Autonomous Agents and Multiagent Systems|AAMAS|
|ACM International Conference on Multimedia|ACM MM|
|Artificial Intelligence and Statistics|AISTATS|
|International Conference on Algorithmic Learning Theory|ALT|
|European Conference on Artificial Intelligence|ECAI|
|Genetic and Evolutionary Computation Conference|GECCO|
|International Conference on Artificial Neural Networks|ICANN|
|International Conference on Automated Planning and Scheduling|ICAPS|
|International Conference on Case-Based Reasoning and Development|ICCBR|
|International Conference on Robotics and Automation|ICRA|
|International Conference on Tools with Artificial Intelligence|ICTAI|
|International Joint Conference on Artificial Intelligence|IJCAI|
|International Joint Conference on Neural Networks|IJCNN|
|International Conference on Intelligent Robots and Systems|IROS|
|International Conference on Principles of Knowledge Representation and Reasoning|KR|
|International conference on Knowledge Science, Engineering and Management|KSEM|
|ACM SIGGRAPH Annual Conference|SIGGRAPH|
|International Conference on Uncertainty in Artificial Intelligence|UAI|
|Parallel Problem Solving from Nature|PPSN|
|Pacific Rim International Conference on Artificial Intelligence|PRICAI|
|International Conference on Technologies and Applications of Artificial Intelligence|TAAI|

### CV

| Full Name | Name |
| ----------- | --- |
|International Conference on 3D Vision|3DV|
|Asian Conference on Computer Vision|ACCV|
|ACM International Conference on Multimedia|ACM MM|
|British machine vision conference|BMVC|
|International Conference on Computer Vision and Pattern Recogintion|CVPR|
|European Conference on Computer Vision|ECCV|
|International Conference on Computer Vision|ICCV|
|International Conference on Document Analysis and Recognition|ICDAR|
|IEEE International Conference on Image Processing|ICIP|
|International conference on multimedia and expo|ICME|
|International Conference on Pattern Recognition|ICPR|
|IEEE visualization conference|IEEE VIS|
|International Conference on Medical Image Computing and Computer Assisted Intervention|MICCAI|
|Neural Information Processing Systems|NeuIPS|
|ACM SIGGRAPH Annual Conference|SIGGRAPH|
|IEEE Winter Conference on Applications of Computer Vision|WACV|


### DM
| Full Name | Name |
| ----------- | --- |
|Automated Knowledge Base Construction|AKBC|
|Asia Pacific Web Conference|APWeb|
|International Conference on Information and Knowledge Management|CIKM|
|Database Systems for Advanced Applications|DASFAA|
|The European Conference on Machine Learning and Principles and Practice of Knowledge Discovery in Databases|ECML-PKDD|
|IEEE International Conference on Data Engineering|ICDE|
|IEEE International Conference on Data Mining|ICDM|
|International Conference on Database Theory|ICDT|
|ACM SIGKDD Conference on Knowledge Discovery and Data Mining|KDD|
|Language Resources and Evaluation Conference|LREC|
|International Conference on Mobile Data Management|MDM|
|Pacific-Asia Conference on Knowledge Discovery and Data Mining|PAKDD|
|ACM Symposium on Principles of Database Systems|PODS|
|The ACM Conference Series on Recommender Systems|RecSys|
|SIAM International Conference on Data Mining|SDM|
|ACM Conference on Management of Data|SIGMOD|
|International Conference on Very Large Data Base|VLDB|
|ACM International Conference on Web Search and Data Mining|WSDM|
|The Web Conference|WWW|

### IR
| Full Name | Name |
| ----------- | --- |
|European Conference on IR Research|ECIR|
|Extended Semantic Web Conference|ESWC|
|ACM International Conference on Multimedia Retrieval|ICMR|
|International Semantic Web Conference|ISWC|
|International Conference on Research on Development in Information Retrieval|SIGIR|


### ML
| Full Name | Name |
| ----------- | --- |
|Asian Conference on Machine Learning|ACML|
|International Conference on Artificial Intelligence and Statistics|AISTATS|
|International Conference on Learning Representations|ICLR|
|International Conference on Machine Learning|ICML|
|Machine Learning for Health|ML4H|
|Neural Information Processing Systems|NeurIPS|
|Conference on Uncertainty in Artificial Intelligence|UAI|

### NLP
| Full Name | Name |
| ----------- | --- |
|Asian Chapter of the Association for Computational Linguistics|AACL|
|Association for Computational Linguistics|ACL|
|Chinese Computational Linguistics|CCL|
|International Conference on Computational Linguistics|COLING|
|Annual Conference on Computational Learning Theory|COLT|
|Conference on Computational Natural Language Learning|CoNLL|
|European Chapter of the Association for Computational Linguistics|EACL|
|Empirical Methods in Natural Language Processing|EMNLP|
|International Conference on Acoustics, Speech and Signal Processing|ICASSP|
|International Conference on Document Analysis and Recognition|ICDAR|
|International Conference on Neural Information Processing|ICONIP|
|Conference of the International Speech Communication Association|INTERSPEECH|
|Language Resources and Evaluation Conference|LREC|
|North American Chapter of the Association for Computational Linguistics|NAACL|
|Natural Language Processing and Chinese Computing|NLPCC|
|SIGdial Meeting on Discourse and Dialogue|SIGDIAL|
|International Workshop on Semantic Evaluation|SemEval|
|Workshop on Arabic natural language processing|WANLP|
|Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis|WASSA|
|Workshop on Online Abuse and Harms|WOAH|


## Adding a new conference

You can manually add any conferences from DBLP to config map.

Take ICLR as an example:

- Step 1: Go to [DBLP](https://dblp.org/db/conf/iclr/iclr2020.html) 
- Step 2: Find the full name of Conference
- Step 3: Add map to ```parserConfig.json```
```json
{"International Conference on Learning Representations": "ICLR"}
```

## Contact

Please email [Libo Qin](mailto:lbqin@ir.hit.edu.cn) or [Qiguang Chen](mailto:charleschen2333@gmail.com) to create Github issues here if you have any questions or suggestions. 

And we welcome you to join us and update conferences at https://docs.qq.com/sheet/DWFF1aWlVV1hISU12?tab=h2idmj 

## Organizers
[Libo Qin](http://ir.hit.edu.cn/~lbqin/); [Qiguang Chen](https://github.com/LightChen233); [Qian Liu](https://siviltaram.github.io/); 

## Contributors

Thanks to the contributors:

[Qi Jia](https://github.com/JiaQiSJTU); [Guanglin Niu](https://github.com/ngl567); [bravery](https://github.com/braveryCHR); [Xiao Xu](https://github.com/LooperXX); [Ruibo Liu](https://github.com/DapangLiu); [Shaolei Zhang](https://github.com/Vily1998); [Shiwen Ni](https://github.com/nishiwen1214);  [Qiming Bao](https://github.com/14H034160212); [Haoyu He](https://github.com/Cli212); [Xuan Zhang](https://github.com/Xzhang1995); [Shining Liang](https://github.com/shiningliang); [Ziyu Jia](https://github.com/ziyujia); [Xin Guo](https://github.com/XinGuoZJU); [Chengbin Hou](https://github.com/houchengbin); [Yuanqi Du](https://yuanqidu.github.io/); [Runze Fan](https://rzfan525.github.io/); [Zayne](https://github.com/ZiYueZH); [Zhiqing Guo](https://github.com/EricGzq); [Jiakai Wang](https://github.com/buaa0110); [Pandeng Li](https://github.com/rovgtjktm66); [Yilun Jin](https://github.com/kl4805); [Yuchen Fang](https://github.com/LMissher); [Yiheng Shu](https://yihengshu.github.io/); [Yichao Du](https://github.com/duyichao); 
