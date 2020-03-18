import requests
from bs4 import BeautifulSoup
import xlwt,xlrd
from xlutils.copy import copy
from tqdm import tqdm

string1 = 'china'
string2 = 'chinese'
string3 = 'beijing'
string4 = 'sino'

Titles = []
Urls = []
for page in tqdm(range(1,38)):
	url = 'https://www.theguardian.com/business/davos?page='+str(page)
	res = requests.get(url)
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,'lxml')
	Category1 = soup.select('section > div > div > div > ul > li > div > div > a')
	Category2 = soup.select('section > div > div > div > ul > li > ul > li > div > div > a')
	for i in Category1:
		Titles.append(i.get_text())
		Urls.append(i.get('href'))
	for i in Category2:
		Titles.append(i.get_text())
		Urls.append(i.get('href'))

Article_num = 0
rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Giardian.xls')
wt = copy(rd)
sh = wt.get_sheet(0)

for i in tqdm(range(len(Urls))):
	if string1 in Titles[i].lower() or string2 in Titles[i].lower() or string3 in Titles[i].lower() or string4 in Titles[i].lower():
		Main = ''
		Time = ''
		res = requests.get(Urls[i])
		res.encoding = 'utf-8'
		soup = BeautifulSoup(res.text,'lxml')
		mains = soup.select('#article > div > div > div > div > p')
		times = soup.select('#article > div > div > div > header > div > div > p > time')
		for j in mains:
			Main += j.get_text() + ' '
		for j in times:
			Time = j.get_text()[-15:-5]
		Article_num += 1
		sh.write(Article_num,0,Article_num)
		sh.write(Article_num,1,Titles[i])
		sh.write(Article_num,2,Time)
		sh.write(Article_num,4,Urls[i])
		sh.write(Article_num,3,Main)
		sh.write(Article_num,6,"Guardian")
		wt.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Giardian.xls')#保存
		print(Article_num)
	else:
		Main = ''
		Time = ''
		res = requests.get(Urls[i])
		res.encoding = 'utf-8'
		soup = BeautifulSoup(res.text,'lxml')
		mains = soup.select('#article > div > div > div > div > p')
		times = soup.select('#article > div > div > div > header > div > div > p > time')
		for j in mains:
			if string1 in j.get_text().lower() or string2 in j.get_text().lower() or string3 in j.get_text().lower() or string4 in j.get_text().lower():
				Main += j.get_text() + ' '
		for j in times:
			Time = j.get_text()[-15:-5]
		if len(Main) > 1:
			Article_num += 1
			sh.write(Article_num,0,Article_num)
			sh.write(Article_num,1,Titles[i])
			sh.write(Article_num,2,Time)
			sh.write(Article_num,4,Urls[i])
			sh.write(Article_num,3,Main)
			sh.write(Article_num,6,"Guardian")
			wt.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Giardian.xls')#保存
			print(Article_num)

print("终止个数：" + str(Article_num))

