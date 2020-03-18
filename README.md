# NLP-national-image-analysis
### Start with spider, end with conclusion.
Massive media news is an important information resource for the national image study in the era of big data, and text mining techniques offer a new approach for identifying national image from news. This paper uses text mining techniques to identify China’s economic image from mass media news on Davos Forum. Specifically, the paper analyzes the basic representations of national image, and uses text mining techniques to identify China’s economic image and the changes. Further, China’s economic images are compared between countries and news media. The results help understand China’s economic images and the changes, and are also potentially meaningful for research and practice on media image of country, region and city.

🌍The original code for BERTSUM by arpytanshu could be found [here](https://github.com/arpytanshu/digiledge-summary-bert)
<br>🤗huggingface repository : [huggingface-transformers](https://github.com/huggingface/transformers)<br>
Model : [bertabs-finetuned-cnndm-extractive-abstractive-summarization](https://huggingface.co/bertabs-finetuned-cnndm-extractive-abstractive-summarization)

### Introduction
#### Data source
  * [Guardian](https://www.theguardian.com/us)
  * [New York Times](https://www.nytimes.com/)
  * [Financial Times](https://www.ft.com/)
  * [Wall-Street Journal](https://www.wsj.com/)
#### Spider modules
  * Selenium
  * Beautiful Soup
#### Data cleaning
  * NLTK 
#### Data analysis
  * Word frequency
  * Word cloud
  * LDA topic model
  * Bert summerization
  * Bert sentiment score
  
###  Module Versions
| module | version | application |
|  ----  | ----  | ---- |
| beautifulsoup | 4.6.3 | spider |
| selenium | 3.141.0 | spider |
| xlrd | 1.1.0 | excel reading |
| xlwt | 1.3.0 | excel writing |
| nltk | 3.4.5 | data cleaning |
| wordcloud | 1.5.0 | word cloud |
| lda | 3.2.5 | LDA topic model |
| transformers | 2.5.1 | summrization & sentiment score |
| torch | 1.4.0 | tensors and dynamic neural networks |
| tqdm | 4.28.1 | progress bar |

### Procedure
<img src="https://github.com/scyyy/NLP-national-image-analysis/blob/master/image/procedure.png" width="500"/>

### Code guide
* Spider
  * Guardian.py
  * New_York_Times.py
  * Financial_Times.py
  * WallStreet_Journal.py
* Data Cleaning
  * NLTK_Proccess.py
* Analysis

 |Code name | Colab URL |
 | --- | --- |
 | Word_frequency | [![open in Colab](https://img.shields.io/badge/open%20in-Colab-orange.svg)](https://colab.research.google.com/github/scyyy/NLP-national-image-analysis/blob/master/analysis/Word_Frequency.ipynb)
 | Word_Cloud | [![open in Colab](https://img.shields.io/badge/open%20in-Colab-orange.svg)](https://colab.research.google.com/github/scyyy/NLP-national-image-analysis/blob/master/analysis/Word_Cloud.ipynb)
 | LDA_topic_model | [![open in Colab](https://img.shields.io/badge/open%20in-Colab-orange.svg)](https://colab.research.google.com/github/scyyy/NLP-national-image-analysis/blob/master/analysis/LDA_topic_model.ipynb)
 | Bert_for_summarization | [![open in Colab](https://img.shields.io/badge/open%20in-Colab-orange.svg)](https://colab.research.google.com/github/scyyy/NLP-national-image-analysis/blob/master/analysis/Bert_for_summarization.ipynb)
 | Bert_for_sentiment | [![open in Colab](https://img.shields.io/badge/open%20in-Colab-orange.svg)](https://colab.research.google.com/github/scyyy/NLP-national-image-analysis/blob/master/analysis/Bert_for_sentiment.ipynb)
---

## 基于达沃斯新闻文本挖掘的中国经济形象分析 ![RUC](http://pic3.58cdn.com.cn/p1/big/n_v1bl2lwtnvxhmvrj4bpima.jpg?w=30&h=22.5)
#### 指导老师：任明
#### **摘要**：媒体新闻是大数据时代的国家形象研究的重要情报资源，而文本挖掘技术为从中识别国家形象开辟了新的渠道。本文使用文本挖掘技术，从达沃斯论坛这一全球重要的经济盛会的西方主流媒体新闻中提取中国的国家经济形象。具体的，本文基于人类对形象的认知分析了国家形象的文字呈现方式，使用相应的文本挖掘方法提取在西方媒体中的中国经济形象及变迁，进一步的对不同国家、不同媒体上的中国经济形象进行对比。相关结果有助于对中国经济形象及变迁的理解，也对大数据时代国家、地区、城市等的媒体形象的研究有借鉴意义。

#### 分类号：G202 G206
