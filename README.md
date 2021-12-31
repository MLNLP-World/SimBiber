# SimBiber: A tool for simplifying bibtex with official info.

We often need to simplify the official bib that consists of many information into a shorter version that only maintains necessary information (e.g., author, title, conference/journal name and etc) due to page limitation.

We introduce __SimBiber__, a simple tool in Python to simplify them automatically. Hope it's helpful for you.

We also highly recommend another wonderful tool for you  [Rebiber](https://github.com/yuchenlin/rebiber), which is a tool for normalizing bibtex with official info.

## Changelog

- **2021.12.31**
We build the first version and release it.

## Installation

```python
git clone https://github.com/MLNLP-World/Simbiber.git
pip install bibtexparser
```

## Usage（v0.1.0）

```bash 
python SimBiberParser.py --input_path data/bibtex.bib --output_path out/bibtex.bib --config_path parserConfig.json --if_append_output False --cache_num 100
```
| argument | usage|
| ----------- | ----------- |
| `--input_path` | The path to the input bib file that you want to simplify |
| `--output_path` | The path to the output bib file that you want to save.  |
| `--config_path` | The path to the mapper config file  |
| `--if_append_output` | Whether append simplified data to output bib file.  |
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

| Name | Full Name |
| --- | ----------- |
| AAAI | Association for the Advance of Artificial Intelligence |
| ACL |  Association for Computational Linguistics |
| CCL |  Chinese Computational Linguistics |
| COLING |  International Conference on Computational Linguistics |
| EMNLP |  Empirical Methods in Natural Language Processing |
| ICASSP | International Conference on Acoustics, Speech and Signal Processing |
| ICLR | International Conference on Learning Representations |
| ICML | International Conference on Machine Learning |
| LREC | Language Resources and Evaluation Conference |
| NeurIPS | Neural Information Processing Systems |
| NLPCC | Natural Language Processing and Chinese Computing |
| SemEval | International Workshop on Semantic Evaluation |
|SIGDIAL| SIGdial Meeting on Discourse and Dialogue|

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

Please email or lbqin@ir.hit.edu.cn or charleschen2333@gmail.com create Github issues here if you have any questions or suggestions. 

## Contributor

Thanks to the contributors:

[Libo Qin](http://ir.hit.edu.cn/~lbqin/); [Qiguang Chen](https://github.com/LightChen233); [Qian Liu](https://siviltaram.github.io/)

