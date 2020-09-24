

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
