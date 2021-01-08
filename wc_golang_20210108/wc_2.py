from bs4 import BeautifulSoup
import urllib.request as req
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

def pmc_scr(article_url_pmc):
    url_1=','.join(article_url_pmc)
    url = url_1
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    article=soup.find_all('p',attrs={'class':'p'})
    article_1 = []
    for t in article:
        article_1.append(t.text)
    mojiretsu = ','.join(article_1)
    return(mojiretsu)
    return(article_1)
def abst(url):
    res = requests.get(url)
    soup=BeautifulSoup(res.text,'html.parser')
    article_1=[]
    meta_tag=soup.find_all('meta', attrs={'name': 'description'})
    for t in meta_tag:
        article_1.append(str(t))
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
from matplotlib import pyplot as plt

with open('text.txt', 'r') as f:
    text = f.read()
STOPWORDS.add('meta')
STOPWORDS.add('content')
STOPWORDS.add('name')
STOPWORDS.add('description')
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



