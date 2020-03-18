from bs4 import BeautifulSoup 
import time
from selenium import webdriver
from tqdm import tqdm
import requests
import xlwt,xlrd
from xlutils.copy import copy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

string1 = 'china'
string2 = 'chinese'
string3 = 'huawei'
string4 = 'beijing'

Article_num = 0
rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_New_York_Times.xls')
wt = copy(rd)
sh = wt.get_sheet(0)

url = 'https://www.nytimes.com/search?dropmab=false&endDate=20200301&query=Davos%20China%20Chinese&sections=Business%7Cnyt%3A%2F%2Fsection%2F0415b2b0-513a-5e78-80da-21ab770cb753%2COpinion%7Cnyt%3A%2F%2Fsection%2Fd7a71185-aa60-5635-bce0-5fab76c7c297%2CWorld%7Cnyt%3A%2F%2Fsection%2F70e865b6-cc70-5181-84c9-8368b3a5c34b%2CBriefing%7Cnyt%3A%2F%2Fsection%2F5d9d446d-41aa-501d-a798-e618095f10c7&sort=best&startDate=20190101'
options = webdriver.ChromeOptions()
prefs={'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/爬虫/chromedriver',options=options)
browser.set_window_size(width=710, height=1200, windowHandle="current")
browser.set_window_position(x=720, y=0)
browser.get(url)
html_text = browser.page_source
soup = BeautifulSoup(html_text,'html.parser')
Article_nums = soup.select('#site-content > div > div.css-1npexfx > div.css-qmql6p > p')
for i in Article_nums:
	Article_num = int(i.get_text()[8:11])
print("共有：" + str(Article_num) + "篇")
Page_switch = int(Article_num/10)
print("需翻页：" + str(Page_switch) + "次")

for PS in tqdm(range(Page_switch)):
	Show_More = browser.find_element_by_xpath('//*[@id="site-content"]/div/div[2]/div[2]/div/button')
	browser.execute_script("arguments[0].click();",Show_More)
	time.sleep(1)

Titles = []
html_text = browser.page_source
soup = BeautifulSoup(html_text,'html.parser')
titles = soup.select('#site-content > div > div > div > ol > li > div > div > div > a > h4')
Urls = soup.select('#site-content > div > div > div > ol > li > div > div > div > a')
Article_num = 0
for i in titles:
	Titles.append(i.get_text().lower())
print(len(Titles))
print(len(Urls))
for i in tqdm(range(len(Titles))):
	if string1 in Titles[i].lower() or string2 in Titles[i].lower() or string3 in Titles[i].lower() or string4 in Titles[i].lower():
		Article_num += 1
		sh.write(Article_num,1,Titles[i])
		# sh.write(Article_num,3,Descriptions[i].get_text())
		sh.write(Article_num,4,'https://www.nytimes.com'+Urls[i].get('href'))
		sh.write(Article_num,5,'New York Times')
		print(Urls[i].get('href')[:4])
		if Urls[i].get('href')[:4] == 'http':
			url = Urls[i].get('href')
		else:
			url = 'https://www.nytimes.com'+Urls[i].get('href')
		print(url)
		res = requests.get(url)
		res.encoding = 'utf-8'
		soup = BeautifulSoup(res.text,'lxml')
		main = ''
		Mains = soup.select('#story > section > div > div > p')
		#story > section > div:nth-child(1) > div > p:nth-child(1)
		for m in Mains:
			main += m.get_text() + ' '
		sh.write(Article_num,3,main)
		Times = soup.select('li.css-i49r68 > time')
		#story > header > div.css-xt80pu.e12qa4dv0 > div > ul > li.css-i49r68 > div > time
		#story > header > div.css-xt80pu.e12qa4dv0 > div.css-18e8msd.epjyd6m0 > ul > li.css-i49r68 > time
		for t in Times:
			if len(t.get_text()) < 5:
				sh.write(Article_num,2,'error')
			else:
				sh.write(Article_num,2,t.get_text())
	else:
		if Urls[i].get('href')[:4] == 'http':
			url = Urls[i].get('href')
		else:
			url = 'https://www.nytimes.com'+Urls[i].get('href')
		print(url)
		res = requests.get(url)
		res.encoding = 'utf-8'
		soup = BeautifulSoup(res.text,'lxml')
		main = ''
		Mains = soup.select('#story > section > div > div > p')
		for m in Mains:
			if string1 in m.get_text().lower() or string2 in m.get_text().lower() or string3 in m.get_text().lower() or string4 in m.get_text().lower():
				main += m.get_text() + ' '
			else:
				pass
		if len(main) >= 4:
			Article_num += 1
			sh.write(Article_num,1,Titles[i])
			# sh.write(Article_num,3,Descriptions[i].get_text())
			sh.write(Article_num,4,'https://www.nytimes.com'+Urls[i].get('href'))
			sh.write(Article_num,5,'New York Times')	
			sh.write(Article_num,3,main)
			Times = soup.select('li.css-i49r68 > time')
			#story > header > div.css-xt80pu.e12qa4dv0 > div > ul > li.css-i49r68 > div > time
			#story > header > div.css-xt80pu.e12qa4dv0 > div.css-18e8msd.epjyd6m0 > ul > li.css-i49r68 > time
			for t in Times:
				if len(t.get_text()) < 5:
					sh.write(Article_num,2,'error')
				else:
					sh.write(Article_num,2,t.get_text())
		else:
			pass
	wt.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_New_York_Times.xls')#保存

