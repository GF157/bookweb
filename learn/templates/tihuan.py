
import pymongo
import re
import pandas as pd

from snownlp import SnowNLP
from string import punctuation

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
seek = book['seekY']
all_info = book['computerY']
sta = book['statistics']


def xiaoshuo(num):
    n = num * 1000
    n = int(n)
    n = n / 1000
    return n

def update_emotion():
    emotion = 0
    count = 0
    for i in all_info.find():
        if i['short']:
            for sh in i['short']:
                sn = SnowNLP(sh)
                for s in sn.sentences:
                    s1 = SnowNLP(s)
                    count += 1
                    emotion += s1.sentiments
            emotion = emotion / count
            all_info.update_many({'_id': i['_id']},{'$set': {'emotion':emotion}})
            print(emotion)
            emotion = 0
            count = 0

# ----------------------------------------------------------------------
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
        count = nation_list.count(i)
        if i == '中' or i == '英':
            count = int(count / 2)
        if i == '日' or i == '法':
            count = int(count * 3)
        data = {
            'nation': i,
            'count': count,
        }
        if nation_list.count(i) > 50 and i != '不明':
            print(data)


def update_tag():
    prog_list = []
    tag = ''
    for i in all_info.find():
        # tag = ''
        if i['label']:
            
            for j in i['label']:
                if j in 'javaJavaJAVA':
                    tag = 'Java'
                if j in 'cc++CC++c语言C语言C/C++':
                    tag = 'C/C++'
                if j in 'pythonPythonPYTHON':
                    tag = 'Python'
                if j in 'phpPhpPHP':
                    tag = 'PHP'
                if j in 'androidAndroidANDROID':
                    tag = 'Android'
                if j in 'webWebWEB网页':
                    tag = 'Web'
            if tag != None and tag != '':

                all_info.update_many({'_id': i['_id']}, {'$set': {'program': tag}})
# update_tag()
