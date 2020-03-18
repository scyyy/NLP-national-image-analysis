import jieba
import xlrd
from tqdm import tqdm
from nltk import word_tokenize
import nltk
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize,pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

import time
import math
import os
import sys
import os, os.path,shutil
import jieba
import jieba.posseg as pseg

global string1,string2
string1 = 'We use cookies for a number of reasons, such as keeping FT Sites reliable and secure, personalising content and ads, providing social media features and to analyse how our Sites are used.'
string2 = 'Comments have not been enabled for this article.'

def jieba_to_string():
	rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/Original_data.xls')
	table = rd.sheets()[0]
	ncols = table.ncols
	Contents = table.col(3, start_rowx=1, end_rowx=None)
	# Titles = table.col(1, start_rowx=1, end_rowx=None)
	# Years = table.col(4, start_rowx=1, end_rowx=None)
	stopwordss = [line.strip() for line in open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据清洗/Stop_words.txt',encoding = 'UTF-8').readlines()]
	fenci_string = ''
	for content in Contents:
		Cleared_article = ''
		fenci = jieba.cut(content.value.replace(string1,'').replace(string2,'').replace('\t',' ').strip(),cut_all = False)
		for i in fenci:
			if i.lower() not in stopwordss:
				if len(i) > 1:
					if i.isdigit() == False:
						Cleared_article += (i.lower()) + ' '
		fenci_string += Cleared_article + '\n'
	print(fenci_string)
	f = open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/data_prepared_string.txt','w')
	f.write(fenci_string)
	return fenci_string

def jieba_to_string_titles():
	rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/Original_data.xls')
	table = rd.sheets()[0]
	ncols = table.ncols
	Contents = table.col(1, start_rowx=1, end_rowx=None)
	# Titles = table.col(1, start_rowx=1, end_rowx=None)
	# Years = table.col(4, start_rowx=1, end_rowx=None)
	stopwordss = [line.strip() for line in open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据清洗/Stop_words.txt',encoding = 'UTF-8').readlines()]
	fenci_string = ''
	for content in Contents:
		Cleared_article = ''
		fenci = jieba.cut(content.value.replace(string1,'').replace(string2,'').replace('\t',' ').strip(),cut_all = False)
		for i in fenci:
			if i.lower() not in stopwordss:
				if len(i) > 1:
					if i.isdigit() == False:
						Cleared_article += (i.lower()) + ' '
		fenci_string += Cleared_article + '\n'
	print(fenci_string)
	f = open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/data_prepared_string_titles.txt','w')
	f.write(fenci_string)
	return fenci_string

def jieba_to_list():
	rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/Original_data.xls')
	table = rd.sheets()[0]
	ncols = table.ncols
	Contents = table.col(3, start_rowx=1, end_rowx=None)
	# Titles = table.col(1, start_rowx=1, end_rowx=None)
	# Years = table.col(4, start_rowx=1, end_rowx=None)
	stopwordss = [line.strip() for line in open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据清洗/Stop_words.txt',encoding = 'UTF-8').readlines()]
	jieba.add_word("dow jones")
	fenci_list = []
	for content in tqdm(range(len(Contents))):
		Cleared_article = []
		fenci = jieba.cut(Contents[content].value.replace(string1,'').replace(string2,'').replace('\t',' ').strip(),cut_all = False)
		for i in fenci:
			if i.lower() not in stopwordss:
				if len(i) > 1:
					if i.isdigit() == False:
						Cleared_article.append(i.lower())
		fenci_list.append(Cleared_article)
	print(str(fenci_list))
	f = open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/data_prepared_list.txt','w')
	f.write(str(fenci_list))

	return str(fenci_list)

def nltk_proccesing():
	stopwordss = [line.strip() for line in open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据清洗/Stop_words.txt',encoding = 'UTF-8').readlines()]
	rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/Original_data.xls')
	table = rd.sheets()[0]
	ncols = table.ncols
	Contents = table.col(3, start_rowx=1, end_rowx=None)
	nltk_split = ''
	for content in Contents:
		token_words = word_tokenize(content.value)
		token_words = pos_tag(token_words)
		words_lematizer = ''
		wordnet_lematizer = WordNetLemmatizer()
		for word, tag in token_words:
		    if tag.startswith('NN'):
		        word_lematizer =  wordnet_lematizer.lemmatize(word, pos='n')  # n代表名词
		    elif tag.startswith('VB'): 
		        word_lematizer =  wordnet_lematizer.lemmatize(word, pos='v')   # v代表动词
		    elif tag.startswith('JJ'): 
		        word_lematizer =  wordnet_lematizer.lemmatize(word, pos='a')   # a代表形容词
		    elif tag.startswith('R'): 
		        word_lematizer =  wordnet_lematizer.lemmatize(word, pos='r')   # r代表代词
		    else: 
		        word_lematizer =  wordnet_lematizer.lemmatize(word)
		    if word_lematizer.lower() not in stopwordss and len(word_lematizer.lower()) > 1 and word_lematizer.isdigit() == False:
		    	words_lematizer += word_lematizer.lower() + ' '
		nltk_split += words_lematizer + '\n'
	print(nltk_split)
	f = open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/data_prepared_nltk_split.txt','w')
	f.write(nltk_split)

# nltk_proccesing()

def CHN_proccessing():
	stopwordss = [line.strip() for line in open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据清洗/Stop_words.txt',encoding = 'UTF-8').readlines()]
	# txtPath = '/Users/scy/Desktop/LinkJing/数据挖掘/From知乎/'
	# # txtPath = txtPath.decode('utf-8')
	# txtType = 'txt'
	# txtLists = os.listdir(txtPath) #列出文件夹下所有的目录与文件
	# txtLists.remove(".DS_Store")
	Articles = ''
	# for file_name in txtLists:
	rd = xlrd.open_workbook('/Users/scy/Desktop/LinkJing/数据挖掘/From知乎/知乎获取_文章马伊琍.xls')
	table = rd.sheets()[0]
	ncols = table.ncols
	Contents = table.col(2, start_rowx=1, end_rowx=None)
	for Content in Contents:
		article = ''
		fenci = jieba.cut(Content.value.strip().replace('\n',' '),cut_all = False)
		for i in fenci:
			if i not in stopwordss:
				if len(i) > 1 and len(i) < 5:
					if i.isdigit() == False:
						article += i + ' '
		Articles += article + '\n'	

	f = open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/data_prepared_CHN_split.txt','w')
	f.write(Articles)

def wrod_2_vec_use():
	stopwordss = [line.strip() for line in open('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据清洗/Stop_words.txt',encoding = 'UTF-8').readlines()]
	rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/Original_data.xls')
	table = rd.sheets()[0]
	ncols = table.ncols
	Contents = table.col(3, start_rowx=1, end_rowx=None)
	nltk_split = ''
	for content in Contents:
		token_words = word_tokenize(content.value)
		print(token_words)

wrod_2_vec_use()

sentence = 'aaaaa？bbbbb。 cccccccddddddddd！'
def cut_sentences(sentence):
    puns = frozenset(u'。！？')
    tmp = []
    for ch in sentence:
        tmp.append(ch)
        if puns.__contains__(ch):
            yield ''.join(tmp)
            tmp = []
    yield ''.join(tmp)

unknow = cut_sentences(sentence)
for i in unknow:
	print(i)
