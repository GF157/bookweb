from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator  # 分页
# Create your views here.
import pymongo
import re
import pandas as pd

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
seek = book['seekY']
all_info = book['computerY']
sta = book['statistics']
info = book['computerZ']
# for i in all_info.find():
# 	if i['number'] and i['number'] != '评分人数不足':
# 		if i['score']:
# 			rank = int(i['number']) * float(i['score'])
# 			print(rank)

# 	else:
# 		rank = 0
# 	all_info.update_many({'_id': i['_id']}, {'$set': {'rank': rank}})

mydoc = all_info.find().sort('rank', -1)
for i in mydoc:
	data = {
    # 书名
    'title': i['title'],

    # 作者
    'author': i['author'],

    # 出版社
    'press': i['press'],

    # 译者
    'trans': i['trans'],

    # 出版年
    'publish_date': i['publish_date'],

    # 页数
    'pages': i['pages'],

    # 定价
    'price': i['price'],

    # 电商价
    'price_d': i['price_d'],

    # 标签
    'label': i['label'],

    # ISBN
    'ISBN': i['ISBN'],

    # 读过的人
    'read': i['read'],

    # 想读的人
    'read_want': i['read_want'],

    # 在读的人
    'reading': i['reading'],

    # 评分
    'score': i['score'],

    # 评分人数
    'number': i['number'],

    # 图书链接
    'url': i['url'],

    # 作者简介
    # 'author_s': i[' 'author_s'],

    # 内容简介
    # 'summary': i[' 'summary'],

    # 读过、想读、在读
    # 'read_box': i[' 'read_box'],

    # 图片链接
    'image': i['image'],

    # 一星
    'one': i['one'],

    # 二星
    'two': i['two'],

    # 三星
    'three': i['three'],

    # 四星
    'four': i['four'],

    # 五星
    'five': i['five'],

    # 短评
    'short': i['short'],

    # 短评数量
    'short_number': i['short_number'],

    # 书评数量
    'book_number': i['book_number'],

    # 笔记数量
    'note_number': i['note_number'],

    'nation': i['nation'],

    'rank': i['rank'],

        }
	info.insert(data)