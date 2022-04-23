<div>
  <h2 align="center">
    <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/ai.png" width="30" />
      SimBiber: A tool for simplifying bibtex with official info.
  </h2>
</div>
<p align="center">
  	<a href="https://img.shields.io/badge/version-v0.7.1-blue">
      <img alt="version" src="https://img.shields.io/badge/version-v0.7.0-blue?color=FF8000?color=009922" />
    </a>
  <a >
       <img alt="Status-building" src="https://img.shields.io/badge/Status-building-blue" />
  	</a>
  <a >
       <img alt="PRs-Welcome" src="https://img.shields.io/badge/PRs-Welcome-red" />
  	</a>
   	<a href="https://github.com/MLNLP-World/SimBiber/stargazers">
       <img alt="stars" src="https://img.shields.io/github/stars/MLNLP-World/SimBiber" />
  	</a>
  	<a href="https://github.com/MLNLP-World/SimBiber/network/members">
       <img alt="FORK" src="https://img.shields.io/github/forks/MLNLP-World/SimBiber?color=FF8000" />
  	</a>
    <a href="https://github.com/MLNLP-World/SimBiber/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/MLNLP-World/SimBiber?color=0088ff"/>
    </a>
    <br />
</p>

------

<div>
<p align="center">
      <a href="#Changelog">Changelog</a> •
      <a href="#Installation">Installation</a> •
      <a href="#Usage">Usage</a> • 
      <a href="#Example Input and Output">Example Input and Output</a> •  
      <a href="#Supported Conferences">Supported Conferences</a> •
      <a href="#Adding a new conference">Adding a new conference</a> •
      <a href="#Contact">Contact</a> •
      <a href="#Organizers">Organizers</a> •
      <a href="#Contributors">Contributors</a> 
    </p>
</div>

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/motivation.png" width="25" /> Motivation
We often need to simplify the official bib that consists of many information into a shorter version that only maintains necessary information (e.g., author, title, conference/journal name and etc) due to page limitation.

We introduce __SimBiber__, a simple tool in Python to simplify them automatically. Hope it's helpful for you.

We also highly recommend another wonderful tool for you [Rebiber](https://github.com/yuchenlin/rebiber), which is a tool for normalizing bibtex with official info.

**Tips**: If you use first Rebiber and then Simbiber, you can get a better experience.

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/disclaimer2.png" width="25" /> Disclaimer

> SimBiber is a fairly new project and it is under active development. 
    We hope that it will be quite useful in a variety of cases, but there is no guarantee that the results it produces will necessarily be strictly compliant with the official specification.
> 
> **So you'd better check the accuracy of simplified bib files again.**
> 
> All icons are collected from the Internet, if there is any infringement, please contact us to delete.




## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/notes.png" width="25" /> Changelog
- **2021.04.23**
  - Support IJCAI (Survey Track).
  - Unified README.
- **2021.04.11**
  - <div style="color: #b0b0b0">Support to <b>pip install</b>.</div>
  - <div style="color: #b0b0b0">Simplify input args.</div>
  - <div style="color: #b0b0b0">Add disclaimer.</div>
- **2021.03.02**
  - <del style="color: #b0b0b0">Fix some bugs if remove duplications.</del>
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


## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/resource.png" width="25" /> Installation

```bash 
git clone https://github.com/MLNLP-World/Simbiber.git
cd Simbiber/
pip install -e .
```
OR
```bash  
pip install simbiber
```

If you would like to use the latest github version with more bug fixes, please use the first installation method.

Finally, if you run ``simbiber`` without any args, you get the following result, then the installation is successful!

<img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/success.jpg" alt=" " style="width:90%" />

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/catalogue.png" width="27" /> Usage(v0.7.1)

```bash 
simbiber -i [input bib path] -o [output bib path]
```
Tips: All path args support absolute and relative paths

| simplified | argument | usage|
|------ | ----------- | ----------- |
|`-i`| `--input_path` | The path to the input bib `file` or `directory` that you want to simplify. |
|`-o`| `--output_path` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span> The path to the output bib file that you want to save. <br/> <b>PLEASE ATTENTION:</b> <ul><li>It only works in simplify single bib file.</li><ul><li>If `output_path==input_path`, it will rewrite input file.</li></ul> <li>Without this param, it will be auto filled:<ul><li>If simplifying single bib `file`, it will rewrite input file;</li> <li>If simplifying bib `directory`, it will output to `./out` dir.</li></ul></li></ul>   |
|`-c`| `--config_path` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span>The path to the mapper config file. The path can be a file directory path, like `config` or a single file path, like `config.json`. <br/> <b>PLEASE ATTENTION:</b> If you want to simplify a huge bib file, you'd better extract external `json` config file to achieve satisfactory speed. |
|`-a`| `--if_append_output` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span> Whether append simplified data to output bib file. |
|`-r`| `--remove_duplicate` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span> Whether remove duplication if your bib has both of arXiv or Conference citation.<br/> <b>PLEASE ATTENTION:</b> If `True`, it might cost more time to write simplified bib file. Please keep patient.  |
|`-cch`| `--cache_num` | <span style="color:#b0b0b0;font-size:10px;">[Optional]</span>The number of bib items you want to simplify at once.<br/> <b>PLEASE ATTENTION:</b> If you want to simplify a huge bib file, you'd better change it to achieve satisfactory speed. |


### Example Input and Output
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

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/folders.png" width="25" /> Supported Conferences 

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
|International Joint Conference on Artificial Intelligence (Survey Track)|IJCAI(Survey Track)|
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


### Adding a new conference

You can manually add any conferences from DBLP to config map.

Take ICLR as an example:

- Step 1: Go to [DBLP](https://dblp.org/db/conf/iclr/iclr2020.html) 
- Step 2: Find the full name of Conference
- Step 3: Add map to ```config/ML.json``` or ```parserConfig.json```(You should specify the config path)
```json
{"International Conference on Learning Representations": "ICLR"}
```

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/intro.png" width="25" /> Contact

Please email [Libo Qin](mailto:lbqin@ir.hit.edu.cn) or [Qiguang Chen](mailto:charleschen2333@gmail.com) to create Github issues here if you have any questions or suggestions. 

And we welcome you to join us and update conferences at https://docs.qq.com/sheet/DWFF1aWlVV1hISU12?tab=h2idmj 

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/organizer.png" width="25" /> Organizers

<a href="https://github.com/yizhen20133868">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Libo Qin.png"  width="80" > </a> 
<a href="https://github.com/LightChen233">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Qiguang Chen2.png"  width="75" > </a> 
<a href="https://github.com/SivilTaram">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Qian.png"  width="80" > </a> 

## <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/heart.png" width="25" /> Contributors
Thanks to the contributors:

<a href="https://github.com/LightChen233">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Qiguang Chen2.png"  width="65" > </a> 
<a href="https://github.com/yizhen20133868">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Libo Qin.png"  width="69" > </a>
<a href="https://github.com/SivilTaram">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Qian.png"  width="69" > </a> 
<a href="http://xcfeng.net/">  <img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/XiaChong Feng.png"  width="60" > </a>
<a href="https://github.com/JiaQiSJTU"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/JiaQiSJTU.png"  width="60" ></a>
<a href="https://github.com/ngl567"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/ngl567.png"  width="60" ></a>
<a href="https://github.com/braveryCHR"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/braveryCHR.png"  width="62" ></a>
<a href="https://github.com/LooperXX"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Xiao Xu.png"  width="69" ></a>
<a href="https://github.com/DapangLiu"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/DapangLiu.png"  width="66" ></a>
<a href="https://github.com/Vily1998"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Vily1998.png"  width="60" ></a>
<a href="https://github.com/nishiwen1214"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/nishiwen1214.png"  width="60" ></a>
<a href="https://github.com/14H034160212"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/14H034160212.png"  width="60" ></a>
<a href="https://github.com/Cli212"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Cli212.png"  width="60" ></a>
<a href="https://github.com/Xzhang1995"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/Xzhang1995.png"  width="60" ></a>
<a href="https://github.com/shiningliang"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/shiningliang.png"  width="60" ></a>
<a href="https://github.com/ziyujia"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/ziyujia.png"  width="60" ></a>
<a href="https://github.com/XinGuoZJU"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/XinGuoZJU.png"  width="60" ></a>
<a href="https://github.com/houchengbin"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/houchengbin.png"  width="60" ></a>
<a href="https://github.com/yuanqidu"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/yuanqidu.png"  width="60" ></a>
<a href="https://github.com/rzfan525"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/rzfan525.png"  width="60" ></a>
<a href="https://github.com/ZiYueZH"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/ZiYueZH.png"  width="60" ></a>
<a href="https://github.com/EricGzq"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/EricGzq.png"  width="60" ></a>
<a href="https://github.com/buaa0110"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/buaa0110.png"  width="60" ></a>
<a href="https://github.com/rovgtjktm66"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/rovgtjktm66.png"  width="60" ></a>
<a href="https://github.com/kl4805"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/kl4805.png"  width="60" ></a>
<a href="https://github.com/LMissher"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/LMissher.png"  width="60" ></a>
<a href="https://github.com/yihengshu"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/yihengshu.png"  width="60" ></a>
<a href="https://github.com/duyichao"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/duyichao.png"  width="60" ></a>
<a href="https://github.com/ryderling"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/ryderling.png"  width="60" ></a>
<a href="https://github.com/hsword"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/hsword.png"  width="60" ></a>
<a href="https://github.com/LauJames"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/LauJames.png"  width="60" ></a>
<a href="http://guangkechen.site"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/guangkechen.png"  width="60" ></a>
<a href="http://https://github.com/ustc-zhu"><img src="https://cdn.jsdelivr.net/gh/LightChen233/blog-img/ustc-zhu.png"  width="60" ></a>

