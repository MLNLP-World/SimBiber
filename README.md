<div align="center">
<img src="figure/MLNLP.png" alt=" " style="width:90%" />
<h2>SimBiber: A tool for simplifying bibtex with official info.</h2>

------

<p align="center">
      <a href="#Changelog">Changelog</a> •
      <a href="#Installation">Installation</a> •
      <a href="#Usage">Usage</a> • 
      <a href="#Example Input and Output">Example Input and Output</a> •  
      <a href="#Supported Conferences">Supported Conferences</a> •
      <a href="#Adding a new conference">Adding a new conference</a> •
      <a href="#Contact">Contact</a> •
      <a href="#Organizers">Organizers</a> •
      <a href="#Contributors">Contributors</a> •
    </p>
</div>


![version](https://img.shields.io/badge/version-v0.5.2-blue)



We often need to simplify the official bib that consists of many information into a shorter version that only maintains necessary information (e.g., author, title, conference/journal name and etc) due to page limitation.

We introduce __SimBiber__, a simple tool in Python to simplify them automatically. Hope it's helpful for you.

We also highly recommend another wonderful tool for you [Rebiber](https://github.com/yuchenlin/rebiber), which is a tool for normalizing bibtex with official info.

**Tips**:If you use Rebiber and then Simbiber can get a better experience.

## Changelog
- **2021.03.02**
  - Fix some bugs if remove duplications.
- **2021.02.15**
  - <del style="color: #b0b0b0">Fix a bug simplify <b>ACL (like EACL)</b> conference to ACL.</del>
  - <div style="color: #b0b0b0">Support <b>ACL Findings</b> and <b>EMNLP findings.</b></div>
- **2021.01.21**
  - <div style="color: #b0b0b0">Support to <b>remove duplication</b> if your bib has some bibitems with same title. (automatically choose Conference citation)</div>
  - <del style="color: #b0b0b0">Fix some bugs about some conferences.</del>
  - <div style="color: #b0b0b0">Add more categories of conferences. (now support 113 conferences)</div>
- **2021.01.11**
  - <del style="color: #b0b0b0">Fix a bug if output path is the same as input path.</del>
  - <del style="color: #b0b0b0">Support to remove duplication if your bib has both of arXiv or Conference citation.</del>
  - <div style="color: #b0b0b0">Support to simplify files <b>by folder</b>.</div>
  - <div style="color: #b0b0b0">Support to use <b>default</b> output path.</div>
  - <del style="color: #b0b0b0">Add more categories of conferences. (now support 112 conferences)</del>
- **2021.01.08**
  <del style="color: #b0b0b0">We fix a bug if booktitle contains `{` or `}` and add more categories of conferences. (now support 105 conferences)</del>
- **2021.01.06**
  <del style="color: #b0b0b0">We fix a few minor bugs and add more categories of conferences. (now support 84 conferences)</del>
- **2021.12.31**
  <del style="color: #b0b0b0">We build the first version and release it.</del>


## Installation

```python
git clone https://github.com/MLNLP-World/Simbiber.git
pip install bibtexparser
```

## Usage(v0.5.1)

```bash 
python SimBiberParser.py --input_path data --config_path config --if_append_output False --cache_num 100 --remove_duplicate True
```
| argument | usage|
| ----------- | ----------- |
| `--input_path` | The path to the input bib `file` or `directory` that you want to simplify. |
| `--output_path` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span> The path to the output bib file that you want to save. <br/> <b>PLEASE ATTENTION:</b> <ul><li>It only works in simplify single bib file.</li><ul><li>If `output_path==input_path`, it will rewrite input file.</li></ul> <li>Without this param, it will be auto filled:<ul><li>If simplifying single bib `file`, it will rewrite input file;</li> <li>If simplifying bib `directory`, it will output to `./out` dir.</li></ul></li></ul>   |
| `--config_path` | The path to the mapper config file. The path can be a file directory path, like `config` or a single file path, like `config.json`. <br/> <b>PLEASE ATTENTION:</b> If you want to simplify a huge bib file, you'd better extract external `json` config file to achieve satisfactory speed. |
| `--if_append_output` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span> Whether append simplified data to output bib file. |
| `--remove_duplicate` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span> Whether remove duplication if your bib has both of arXiv or Conference citation.<br/> <b>PLEASE ATTENTION:</b> If `True`, it might cost more time to write simplified bib file. Please keep patient.  |
| `--cache_num` | The number of bib items you want to simplify at once.<br/> <b>PLEASE ATTENTION:</b> If you want to simplify a huge bib file, you'd better change it to achieve satisfactory speed. |


## Example Input and Output
An example simplified output entry with the official information (The forms of bibitem like `xxx="..."` or `xxx={...}` are both supported):
```bib
@inproceedings{li-etal-2019-survey,
    title = "A Sophisticated Survey about Chinese Poem and Beers",
    author = "Li, Bai  and
     Ha, Pi  and
     Jin, Shibai  and
     Xue, Hua  and
     Mao, Tai",
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
@inproceedings{li-etal-2019-survey,
    author = {Li, Bai  and
     Ha, Pi  and
     Jin, Shibai  and
     Xue, Hua  and
     Mao, Tai},
    booktitle = {Proc. of EMNLP},
    title = {A Sophisticated Survey about Chinese Poem and Beers},
    year = {2019}
}
```


## Supported Conferences 

The `config` dir contains a list of converted json files of the mapper between official full name and simplified name.

### AI

| Full Name | Name |
| --- | ----------- |
|Association for the Advance of Artificial Intelligence|AAAI|
|International Joint Conference on Autonomous Agents and Multiagent Systems|AAMAS|
|ACM International Conference on Multimedia|ACM MM|
|Artificial Intelligence and Statistics|AISTATS|
|International Conference on Algorithmic Learning Theory|ALT|
|IEEE Congress on Evolutionary Computation|CEC|
|European Conference on Artificial Intelligence|ECAI|
|IEEE International Conference on Fuzzy Systems|FUZZ IEEE|
|Genetic and Evolutionary Computation Conference|GECCO|
|International Conference on Artificial Neural Networks|ICANN|
|International Conference on Automated Planning and Scheduling|ICAPS|
|International Conference on Case-Based Reasoning and Development|ICCBR|
|International Conference on Neural Information Processing|ICONIP|
|International Conference on Robotics and Automation|ICRA|
|International Conference on Tools with Artificial Intelligence|ICTAI|
|International Joint Conference on Artificial Intelligence|IJCAI|
|International Joint Conference on Neural Networks|IJCNN|
|International Conference on Intelligent Robots and Systems|IROS|
|International Conference on Principles of Knowledge Representation and Reasoning|KR|
|International conference on Knowledge Science, Engineering and Management|KSEM|
|ACM SIGGRAPH Annual Conference|SIGGRAPH|
|ACM Symposium on Theory of Computing|STOC|
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
|International Conference on Medical Image Computing and Computer Assisted Intervention Society|MICCAI|
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
|ACM SIGMOD international conference on Management of data|SIGMOD|
|International Conference on Very Large Data Base|VLDB|
|ACM International Conference on Web Search and Data Mining|WSDM|
|The Web Conference|WWW|
|International Conference on Extending DB Technology|EDBT|
|International Conference on Innovative Data Systems Research|CIDR|

### IR
| Full Name | Name |
| ----------- | --- |
|European Conference on IR Research|ECIR|
|Extended Semantic Web Conference|ESWC|
|ACM International Conference on Multimedia Retrieval|ICMR|
|The ACM SIGIR International Conference on the Theory of Information Retrieval|ICTIR|
|International Semantic Web Conference|ISWC|
|International Conference on Research on Development in Information Retrieval|SIGIR|

### ML
| Full Name | Name |
| ----------- | --- |
|Asian Conference on Machine Learning|ACML|
|International Conference on Artificial Intelligence and Statistics|AISTATS|
|European Conference on Machine Learning|ECML|
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
|Workshop on Representation Learning for NLP|RepL4NLP|
|SIGdial Meeting on Discourse and Dialogue|SIGDIAL|
|International Workshop on Semantic Evaluation|SemEval|
|Workshop on Arabic natural language processing|WANLP|
|Workshop on Computational Approaches to Subjectivity, Sentiment and Social Media Analysis|WASSA|
|Workshop on Online Abuse and Harms|WOAH|

### Arch
| Full Name | Name |
| ----------- | --- |
|International Conference on Architectural Support for Programming Languages and Operating Systems|ASPLOS|
|USENIX Annul Technical Conference|ATC|
|Design, Automation & Test in Europe|DATE|
|European Conference on Computer Systems|EuroSys|
|Conference on File and Storage Technologies|FAST|
|High Performance Computer Architecture|HPCA|
|International Symposium on Computer Architecture|ISCA|
|IEEE/ACM International Symposium on Microarchitecture|MICRO|
|ACM SIGPLAN Symposium on Principles & Practice of Parallel Programming|PPoPP|
|International Conference for High Performance Computing, Networking, Storage, and Analysis|SC|
|ACM Symposium on Cloud Computing|SoCC|

### System
| Full Name | Name |
| ----------- | --- |
|ACM SIGSOFT Symposium on the Foundation of Software Engineering/ European Software Engineering Conference|FSE/ESEC|
|International Conference on Software Engineering|ICSE|
|International Symposium on Software Testing and Analysis|ISSTA|
|USENIX Symposium on Operating Systems Design and Implementations|OSDI|
|ACM Symposium on Operating Systems Principles|SOSP|


### Security
| Full Name | Name |
| ----------- | --- |
|Annual Computer Security Applications Conference|ACSA|
|ACM Asia Conference on Computer and Communications Security|AsiaCCS|
|ACM Conference on Computer and Communications Security|CCS|
|Dependable Systems and Networks|DSN|
|European Symposium on Research in Computer Security|ESORICS|
|European Symposium on Security and Privacy|EuroS&P|
|International Conference on Information and Communication Security|ICICS|
|Network and Distributed System Security Symposium|NDSS|
|International Symposium on Recent Advances in Intrusion Detection|RAID|
|IEEE Symposium on Security and Privacy|SP|
|Usenix Security Symposium|USENIX Security|


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

[Qi Jia](https://github.com/JiaQiSJTU); [Guanglin Niu](https://github.com/ngl567); [bravery](https://github.com/braveryCHR); [Xiao Xu](https://github.com/LooperXX); [Ruibo Liu](https://github.com/DapangLiu); [Shaolei Zhang](https://github.com/Vily1998); [Shiwen Ni](https://github.com/nishiwen1214);  [Qiming Bao](https://github.com/14H034160212); [Haoyu He](https://github.com/Cli212); [Xuan Zhang](https://github.com/Xzhang1995); 

[Shining Liang](https://github.com/shiningliang); [Ziyu Jia](https://github.com/ziyujia); [Xin Guo](https://github.com/XinGuoZJU); [Chengbin Hou](https://github.com/houchengbin); [Yuanqi Du](https://yuanqidu.github.io/); [Runze Fan](https://rzfan525.github.io/); [Zayne](https://github.com/ZiYueZH); [Zhiqing Guo](https://github.com/EricGzq); [Jiakai Wang](https://github.com/buaa0110); [Pandeng Li](https://github.com/rovgtjktm66); 

[Yilun Jin](https://github.com/kl4805); [Yuchen Fang](https://github.com/LMissher); [Yiheng Shu](https://yihengshu.github.io/); [Yichao Du](https://github.com/duyichao); [Ryder](https://github.com/ryderling); [Xupeng Miao](https://hsword.github.io); [Jiawei Liu](https://github.com/LauJames); [Guangke Chen](http://guangkechen.site/); [Guanqi Zhu](https://github.com/ustc-zhu)

## Disclaimer

SimBiber is a fairly new project and it is under active development. 
We hope that it will be quite useful in a variety of cases, but there is no guarantee that the results it produces will necessarily be strictly compliant with the official specification.

<div style="color: red"><b>So you'd better check the accuracy of simplified bib files again.</b></div>