from bs4 import BeautifulSoup
import requests
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

string1 = 'china'
string2 = 'chinese'
string3 = 'Beijing'
string4 = 'huawei'

options = webdriver.ChromeOptions()
options.add_argument('User-Agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3","Accept-Encoding":"gzip","Accept-Language":"zh-CN,zh;q=0.9","Cache-Control":"max-age=30","Upgrade-Insecure-Requests":"1')
prefs={'profile.default_content_setting_values': {'images': 2}}
options.add_experimental_option('prefs',prefs)
browser = webdriver.Chrome('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/爬虫/chromedriver',options=options)
browser.set_window_size(width=710, height=1200, windowHandle="current")
browser.set_window_position(x=720, y=0)
browser.get('https://www.wsj.com/search/term.html?KEYWORDS=Davos%20China&min-date=2019/01/01&max-date=2020/03/01&isAdvanced=true&daysback=1y&meta=China&andor=AND&sort=date-desc&source=wsjarticle,wsjblogs,wsjvideo,interactivemedia,sitesearch,wsjpro&page=4')
time.sleep(15)                  
Sign_in = browser.find_element_by_xpath('//*[@id="full-header"]/div/div/div/header/div[2]/a[2]')
browser.execute_script("arguments[0].click();",Sign_in)
browser.find_element_by_id("username").clear()
browser.find_element_by_id("username").send_keys("jianyangsong1998@163.com")
browser.find_element_by_id("password").clear()
browser.find_element_by_id("password").send_keys("19980530HUhu")
Next = browser.find_element_by_xpath('//*[@id="basic-login"]/div[1]/form/div/div[6]/div[1]/button')
browser.execute_script("arguments[0].click();",Next)
time.sleep(5)
Continue = browser.find_element_by_xpath('//*[@id="email-verification"]/div/div[2]/div/div[2]/div/div/button[2]')
browser.execute_script("arguments[0].click();",Continue)

Article_num = 53
rd = xlrd.open_workbook('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Wallstreet_Journal.xls')
wt = copy(rd)
sh = wt.get_sheet(0)
for page in range(1,12):
	for number in range(1,21):
		
		main = ''
		html_text = browser.page_source
		soup = BeautifulSoup(html_text,'html.parser')
        #main > div > div.search-results-sector > div > div > ul > li:nth-child(1) > div > div > h3 > a
		title = soup.select('#main > div > div.search-results-sector > div > div > ul > li:nth-of-type('+str(number)+') > div > div > h3 > a')
		times = soup.select('#main > div > div.search-results-sector > div > div > ul > li:nth-of-type('+str(number)+') > div > div > div > ul > li > time')
		for i in title:
			Title = i.get_text()
			Href = 'https://www.wsj.com' + i.get('href')
		for i in times:
			Time = i.get_text()
#             //*[@id="main"]/div/div[2]/div/div/ul/li[1]/div/div/h3/a
		try:
			Article = browser.find_element_by_xpath('//*[@id="main"]/div/div[2]/div/div/ul/li['+str(number)+']/div/div/h3/a')
		except NoSuchElementException:
			browser.refresh()
		finally:
			browser.execute_script("arguments[0].click();",Article)
			time.sleep(2)	

		if string1 in Title.lower() or string2 in Title.lower() or string3 in Title.lower() or string4 in Title.lower():
			html_text = browser.page_source
			soup = BeautifulSoup(html_text,'html.parser')
			mains1 = soup.select('#wsj-article-wrap > div.article-content > p')
			for i in mains1:
				main += ' ' + i.get_text().replace("\n"," ")
			mains2 = soup.select('#wsj-article-wrap > div.article-content > div > p')
			for i in mains2:
				main += ' ' + i.get_text().replace("\n"," ")
		else:
			html_text = browser.page_source
			soup = BeautifulSoup(html_text,'html.parser')
			mains1 = soup.select('#wsj-article-wrap > div.article-content > p')
			for i in mains1:
				if string1 in i.get_text().lower() or string2 in i.get_text().lower() or string3 in i.get_text().lower() or string4 in i.get_text().lower():
					main += ' ' + i.get_text().replace("\n"," ")
			mains2 = soup.select('#wsj-article-wrap > div.article-content > div > p')
			for i in mains2:
				if string1 in i.get_text().lower() or string2 in i.get_text().lower() or string3 in i.get_text().lower() or string4 in i.get_text().lower():
					main += ' ' + i.get_text().replace("\n"," ")
		
		if string1 in Title.lower() or string2 in Title.lower() or string3 in Title.lower() or string4 in Title.lower() or string1 in main.lower() or string2 in main.lower() or string3 in main.lower() or string4 in main.lower():
			Article_num += 1
			sh.write(Article_num,0,Article_num)
			sh.write(Article_num,3,main)
			sh.write(Article_num,1,Title)
			sh.write(Article_num,2,Time)
			sh.write(Article_num,4,Href)
			sh.write(Article_num,6,"Wall-street Journal")
		wt.save('/Users/scy/Desktop/基于达沃斯新闻文本挖掘的中国国家经济形象研究/数据获取/数据/1920_Wallstreet_Journal.xls')#保存
		browser.back()
		print(Article_num)
		time.sleep(1)
	Next_page = browser.find_element_by_xpath('/html/body/div[2]/div[5]/section[3]/div[1]/div[2]/div/div/div[2]/menu/li[5]/a')
	browser.execute_script("arguments[0].click();",Next_page)
print("Finished")
browser.quit()
