from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator # 分页
# Create your views here.
from learn.models import Modouban
import pymongo
import re
import pandas as pd

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
seek = book['seekY']
all_info = book['computerY']
sta = book['statistics']


def obtain_date(label):
    pro_list = [0, 0, 0, 0]
    for i in seek.find():
        if i['publish_date'] and i['label'] and i['tag']:
            try:
                time = re.findall('(\d\d\d\d)', i['publish_date'])[0]
            except:
                time = 0
            if time != 0 and i['tag'] == label:

                if int(time) > 1900 and int(time) < 1999:
                    pro_list[0] += 1
                if int(time) > 2000 and int(time) < 2009:
                    pro_list[1] += 1
                if int(time) > 2010 and int(time) < 2014:
                    pro_list[2] += 1
                if int(time) > 2015 and int(time) < 2019:
                    pro_list[3] += 1
    data = {
        'name': label,
        'data': pro_list,
    }
    return data

def get_pro():
    yield obtain_date('python')
    yield obtain_date('java')
    yield obtain_date('c++')

# 编程语言
# test = [data for data in get_pro()]
# for i in test:
#     print(i)

def get_nation():
    nation_list = []
    nation_index = []
    naiton_count = []
    for i in all_info.find():
        nation_list.append(i['nation'])
    nation_index = list(set(nation_list))
    for i in nation_index:
        naiton_count.append(nation_list.count(i))
        data = {
            'nation': i,
            'count': nation_list.count(i),
        }
        if nation_list.count(i) > 50:
            print(data)

get_nation()
