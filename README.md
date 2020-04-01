
# 基于达沃斯新闻文本挖掘的中国经济形象分析 ![RUC](http://pic3.58cdn.com.cn/p1/big/n_v1bl2lwtnvxhmvrj4bpima.jpg?w=30&h=22.5)
#### 指导老师：任明
#### **摘要：**  媒体新闻是大数据时代为背景的国家形象研究的重要情报资源。近年来，快速发展的文本挖掘技术为基于媒体新闻的国家形象识别开辟了新的渠道。本文首先基于人类对形象的认知分析了国家媒体形象的文字呈现方式，以议题、观点和态度三方面为切入点，提出使用相应的文本挖掘方法提取国家媒体形象，进一步以达沃斯论坛这一全球重要的经济盛会中，西方主流媒体对中国的新闻报道为例，分析2005年至2020年期间传播的中国国家经济形象。本研究将文本挖掘模型的输出与历史事件相结合进行分析，使试验结果更具有实践意义。文中采用质性方法和量化方法得到的相关结果有助于对中国经济形象及变化的理解，也对大数据时代中的国家、地区、城市等媒体形象的研究有借鉴意义。
#### 关键词：文本挖掘；经济形象；新闻；中国；达沃斯论坛
#### 分类号：G202 G206
---
# NLP-national-image-analysis
### Start with spider, end with conclusion.
Entering a new era of big data, media news has become an increasingly important information resource for researches in national image. In recent years, the fast development of text mining technology has enabled us to analyze national image through media news. Based on human cognition of image, this paper first illustrates the topics, standpoints and attitudes of the literal presentation concerning national media image. Then focusing on Chinese economic image from 2005 to 2020 as an example, this paper advances by using proper text mining method to extract the image from western mainstream media news regarding Davos Forum. This paper combines the presentation of text mining model with the analysis of historical events, thus making the research results more practical. The relevant conclusions obtained in this paper through qualitative and quantitative methods not only contribute to the understanding of China’s economic image, but also offer referential value in the study of the media image of certain country, region or city in the era of big data.

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
