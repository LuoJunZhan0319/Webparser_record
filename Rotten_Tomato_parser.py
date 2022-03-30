#!/usr/bin/env python
# coding: utf-8

# In[125]:


from selenium.webdriver.common.keys import Keys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
review = [] #評論儲存空間

#模擬環境
movie=input("查詢評分的電影:")

#搜尋網址製作
rottentomatoes_url = "https://www.rottentomatoes.com/search?search="
search_url = rottentomatoes_url+movie.replace(" ","%20")

#get網址並解析網址
soup = BeautifulSoup(requests.get(search_url).text, 'html.parser')

#抓取電影網址
import re    #利用正規表達式
urls = soup.find("a", href=re.compile("https://www.rottentomatoes.com/m/.*")) 
movie_herf = urls.get("href")

#建立電影關鍵評論網址
reviews_url = movie_herf+"/reviews"

#利用selenium爬取資料
PATH = "C:/Users/toby/chromedriver_win32/chromedriver.exe" #chromedriver 路徑
driver = webdriver.Chrome(PATH) #建立chromedriver 物件
driver.get(reviews_url) #開啟網址

urls = driver.find_elements_by_class_name("the_review")

for i in urls:
    review.append(i.text)

#換頁按鈕
next_botton = driver.find_element_by_xpath('//*[@id="content"]/div/div/div/nav[2]/button[2]')    

a=0
while(a==0):
    
    try:   
        #點擊煥頁鈕
        next_botton.click()
        time.sleep(2)
        #抓文章
        urls = driver.find_elements_by_class_name("the_review")
        #儲存
        for i in urls:
            review.append(i.text)
        
    except:
        a=1 #遇到例外就停止

driver.quit()


# In[ ]:




