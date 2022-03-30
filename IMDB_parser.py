#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#記錄用，裡面需要install的套件有requests,bs4,selenium
#其中selenium需要配合driver做使用、依據你會使用瀏覽器安裝即可
#因資料室利用google chrom抓取，故需載入chromdriver，版本可查詢你使用的對應瀏覽器本版即可
#若都有安裝，下列程式皆可正常執行

########################################
#讀取資料的方法
# c = []
# with open('inside out.txt', 'r',encoding="utf-8") as f:
#     a = f.readlines()

# for i in a:
#     c.append(i)
########################################


# In[ ]:


import requests
from bs4 import BeautifulSoup
import time
import selenium
from selenium import webdriver

review = [] #評論儲存空間

#模擬環境
movie=input("想查詢那部電影的評分:")

#搜尋網址製作
search_url = "https://www.imdb.com/find?q="+movie.replace(" ","+")+"&ref_=nv_sr_sm"

#get網址並解析網址
soup = BeautifulSoup(requests.get(search_url).text, 'html.parser')

#抓出電影網址
urls = soup.find("td",class_="result_text")
movie_href = urls.a.get("href")
reviews_url = "https://www.imdb.com/"+movie_href+"reviews"

#使用selenium
PATH = "C:/Users/toby/chromedriver_win32/chromedriver.exe" #chromedriver 路徑
driver = webdriver.Chrome(PATH) #建立chromedriver 物件
driver.get(reviews_url)

#就瘋狂點more
a=0
while(a==0):
    try:
        next_botton = driver.find_element_by_xpath('//*[@id="load-more-trigger"]')
        next_botton.click()
        time.sleep(2)
        
    except:
        a=1

#把點完網頁載入，並解析
html = driver.page_source
soup = BeautifulSoup(html, 'html5lib')
#爬取評論並儲存
urls = soup.find_all("div",class_="text show-more__control")
for i in urls:
    review.append(i.text)
#關閉    
driver.quit()

#儲存成txt檔 ->檔案會在當前檔案位置
with open(movie+'.txt', 'w',encoding="utf-8") as f:
    for i in review:
        f.write(i)
        f.write("\n")

