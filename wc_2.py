from bs4 import BeautifulSoup
import urllib.request as req
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import chromedriver_binary
from webdriver_manager.chrome import ChromeDriverManager
import requests
import sys

x = sys.argv
url=x[1]
response=req.urlopen(url)

parse_html=BeautifulSoup(response,'html.parser')

title=parse_html.find_all('a')
url_list=[]
for i in title:
        url_list.append(i.attrs['href'])

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True
options = Options()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu');
options.add_argument('--disable-extensions');
options.add_argument('--proxy-server="direct://"');
options.add_argument('--proxy-bypass-list=*');
options.add_argument('--start-maximized');
options.add_argument('--headless'); 

driver = webdriver.Chrome(ChromeDriverManager(version="87.0.4280.88").install(),chrome_options=options, desired_capabilities=capabilities)
def pmc_scr(article_url_pmc):
    url_1=','.join(article_url_pmc)
    url = url_1
    driver.get(url)
    article = driver.find_elements_by_class_name("jig-ncbiinpagenav")
    article_1 = []
    for t in article:
        article_1.append(t.text)
    mojiretsu = ','.join(article_1)
    return(mojiretsu)
def abst(url):
    driver.get(url)
    article = driver.find_elements_by_class_name("abstract")
    article_1 = []
    for t in article:
        article_1.append(t.text)
    mojiretsu = ','.join(article_1)
    return(mojiretsu)
article_url_pmc=[]
article_url_pmc=[s for s in url_list if 'article' in s]
if article_url_pmc:
    a=pmc_scr(article_url_pmc)
else:
    a=abst(url)
f = open('text.txt', 'w')
f.write(a)
f.close()

from wordcloud import WordCloud
from wordcloud import STOPWORDS


with open('text.txt', 'r') as f:
    text = f.read()
STOPWORDS.add('meta')
STOPWORDS.add('content')
STOPWORDS.add('name')
STOPWORDS.add('description')
STOPWORDS.add('meta')
STOPWORDS.add('pubmed')
STOPWORDS.add('scholar')
STOPWORDS.add('google')
STOPWORDS.add('pmc')
STOPWORDS.add('study')
wc = WordCloud(
    width=480, 
    height=320, 
    background_color="white", 
    prefer_horizontal=1.0, 
    min_word_length=3,
    max_words=40,
    font_path='SFNSDisplayCondensed-Bold.otf',)
wc.generate(text)
wc.to_file('wc.png')

import boto3

BUCKET = 'wc.project'
KEY = 'wc.png'

s3 = boto3.resource('s3')
s3.Bucket(BUCKET).upload_file(Filename=KEY, Key=KEY, ExtraArgs={'ACL':'public-read'})



