from bs4 import BeautifulSoup 
import pandas as pd
import time
from tqdm import tqdm
import requests
import xlwt,xlrd
from xlutils.copy import copy
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# 变量设置
Titles = []
Times = []
Hrefs = []
Mains = []
string1 = 'china'
string2 = 'chinese'
string3 = 'Beijing'
string4 = 'sino'

# 模拟浏览器设置
Cookie = {'domain': '.ft.com', 'expiry': 1615312807.874614, 'httpOnly': False, 'name': 'FTAllocation', 'path': '/', 'secure': False, 'value': '6d9d916e-beb6-43e6-9d74-48c77c2539e5'}, {'domain': '.ft.com', 'expiry': 1590247744.265047, 'httpOnly': False, 'name': 'FTSession_s', 'path': '/', 'secure': True, 'value': 'z22dkW6-tkPm0510SMd8JTnlzwAAAW6Y4XZGw8I.MEUCIQD44HBK_PRIS_TgKuo2crB4Lspcz8_gtVHaVBGwOx4XqQIgDLScNvlk36P9ykZAgbDzomBEGcSU3amBFJLczHR87SU'}, {'domain': '.ft.com', 'expiry': 1590247744.265102, 'httpOnly': False, 'name': 'FTLogin', 'path': '/', 'secure': False, 'value': 'beta'}, {'domain': '.ft.com', 'httpOnly': True, 'name': '_csrf', 'path': '/', 'secure': True, 'value': 'W5rUTFiLrq7TeJ-geq6PXg50'}, {'domain': '.ft.com', 'expiry': 1575127833.553609, 'httpOnly': False, 'name': 'o-typography-fonts-loaded', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.ft.com', 'expiry': 1889883033, 'httpOnly': False, 'name': 'spoor-id', 'path': '/', 'secure': False, 'value': 'ck3bq4qoc00003h5swfq7ckwd'}, {'domain': '.ft.com', 'expiry': 1590247744.264984, 'httpOnly': False, 'name': 'FTSession', 'path': '/', 'secure': False, 'value': 'z22dkW6-tkPm0510SMd8JTnlzwAAAW6Y4Xo-w8I.MEUCICzhv72BrKBJWyQ5mICPRbrXB6OTy2qmOhmsdO37SpfdAiEAg72gQEDx4XMnnYTLLlxOjrVArM5vNWzj8_HGCWs8AiQ'}, {'domain': '.ft.com', 'expiry': 1637594649, 'httpOnly': False, 'name': '__gads', 'path': '/', 'secure': False, 'value': 'ID=56bf874478b3f33d:T=1574522649:S=ALNI_MaOQOGoqipF0Bd-NW4MkCxIKqn_lw'}, {'domain': '.ft.com', 'expiry': 1582298648, 'httpOnly': False, 'name': '_gcl_au', 'path': '/', 'secure': False, 'value': '1.1.352647120.1574522648'}
options = webdriver.ChromeOptions()
options.add_argument('User-Agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Accept-Encoding":"gzip","Accept-Language":"zh-CN,zh;q=0.9","Cache-Control":"max-age=30","Upgrade-Insecure-Requests":"1')
prefs={'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/爬虫/chromedriver',options=options)
browser.set_window_size(width=710, height=1200, windowHandle="current")
browser.set_window_position(x=720, y=0)
# options.add_argument("--proxy-server=http://202.20.16.82:10152")
browser.get('https://www.ft.com/search?q=Davos%20China&page=9&dateTo=2020-03-01&dateFrom=2019-01-01&sort=relevance&expandRefinements=true')

# 添加cookie
for i in range(len(Cookie)):
	if 'expiry' in Cookie[i]:
		del Cookie[i]['expiry']
		if 'domain' in Cookie[i]:
			del Cookie[i]['domain']
			browser.add_cookie(Cookie[i])
time.sleep(2)
browser.refresh()

# 创建excel
# wb = xlwt.Workbook()
# sh = wb.add_sheet('test_1')
# sh.write(0,0,'Titles')
# sh.write(0,1,'Times')
# sh.write(0,2,'Mains')
# sh.write(0,3,'Urls')
# wb.save('/Users/scy/Desktop/Python/Davos/Financial Times/Final_result.xls')#保存

# 获取文章标题、链接、时间
Article_num = 142
rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Financial_Times.xls')
wt = copy(rd)
sh = wt.get_sheet(0)
for Pages in range(1,40):
	for number in range(1,25):
		html_text = browser.page_source
		soup = BeautifulSoup(html_text,'html.parser')
		pro = soup.select('#site-content > div > ul > li:nth-of-type('+str(number)+') > div > div > div > div.o-teaser__content > div.o-teaser__heading > span')
		proing = ''
		for i in pro:
			proing = i.get_text()
		# print(proing)
		# print(len(proing))
		if proing != ' Premium' :
			main = ''
			titles = soup.select('#site-content > div > ul > li:nth-of-type('+str(number)+') > div > div > div > div.o-teaser__content > div.o-teaser__heading > a')
			times = soup.select('#site-content > div > ul > li:nth-of-type('+str(number)+') > div > div > div > div.o-teaser__content > div.o-teaser__timestamp > time')
			for i in titles:
				Title = i.get_text()
				Href = 'https://www.ft.com' + i.get('href')
			for i in times:
				Time = i.get_text()
			Article = browser.find_element_by_xpath('//*[@id="site-content"]/div/ul/li['+str(number)+']/div/div/div/div[1]/div[2]/a')
			browser.execute_script("arguments[0].click();",Article)		
			if string1 in Title.lower() or string2 in Title.lower() or string3 in Title.lower() or string4 in Title.lower():
				html_text = browser.page_source
				soup = BeautifulSoup(html_text,'html.parser')
				mains = soup.select('#site-content > div.article__content > div.article__content-body.n-content-body.js-article__content-body > p')		   	   
				for i in mains:
					main += ' ' + i.get_text()
			else:
				html_text = browser.page_source
				soup = BeautifulSoup(html_text,'html.parser')
				mains = soup.select('#site-content > div.article__content > div.article__content-body.n-content-body.js-article__content-body > p')		   	   
				for i in mains:
					if string1 in i.get_text().lower() or string2 in i.get_text().lower() or string3 in i.get_text().lower() or string4 in i.get_text().lower():
						main += ' ' + i.get_text()
			if string1 in Title.lower() or string2 in Title.lower() or string3 in Title.lower() or string4 in Title.lower() or string1 in main.lower() or string2 in main.lower() or string3 in main.lower() or string4 in main.lower():
				Article_num += 1
				sh.write(Article_num,0,Article_num)
				sh.write(Article_num,1,Title)
				sh.write(Article_num,2,Time)
				sh.write(Article_num,4,Href)
				sh.write(Article_num,3,main)
				sh.write(Article_num,6,"Financial Times")
				wt.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Financial_Times.xls')#保存
			print(Article_num)
			browser.back()
			time.sleep(1)
		else:
			pass
	Next_page = browser.find_element_by_xpath('//*[@id="site-content"]/div/div[4]/div/a[2]')
	browser.execute_script("arguments[0].click();",Next_page)

print('终止个数：' + str(Article_num))
