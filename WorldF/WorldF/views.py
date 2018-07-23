from django.shortcuts import render

import requests   # Web からデータを取ってくる時に使う

import bs4        # スクレイピング

import re         # 正規表現によるマッチングを使う

import random



def appmain(request):

    res = requests.get('https://news.yahoo.co.jp/list/')
    soup = bs4.BeautifulSoup(res.text, "html5lib")
    news = soup.findAll('li', class_='ListBoxwrap')
    urls = []
    for i in range(len(news)):
        urls.append(news[i].a.attrs['href'])

    res2 = requests.get(random.choice(urls))
    soup2 = bs4.BeautifulSoup(res2.text, "html5lib")
    title = soup2.h1.text
    des = soup2.findAll('p', class_='hbody')[0].text
    

    return render(request, 'demo/main.html', {

        'answer' : title,

        'descr' : des,

    })
