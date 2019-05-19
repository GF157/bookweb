from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator # 分页
# Create your views here.
from learn.models import Modouban
import pymongo
import re

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
all_info = book['computerY']
sta = book['statistics']

# 所有数据
author_list = []
press_list = []
label_list = []

# 不重复数据
author_index =[]
press_index = []
label_index = []

# 出现次数
author_count = []
press_count = []
label_count = []


# 清洗数据库
for i in all_info.find().limit(10426):

    # 作者
    if i['author']:
        author = i['author']
    else:
        author = '不明'
    if i['author'] == '0':
        author = '不明'

    # 出版社
    if i['press']:
        press = i['press']
    else:
        press = '不明'
    if i['press'] == '0':
        press = '不明'

    # 标签
    if i['label']:
        for tag in i['label']:
            label_list.append(tag)

    author_list.append(i['author'])
    press_list.append(i['press'])



    # 更新数据
    # all_info.update_many({'_id': i['_id']}, {'$set': {'author': author}})
    # all_info.update_many({'_id': i['_id']}, {'$set': {'press': press}})





author_index = list(set(author_list))
press_index = list(set(press_list))
label_index = list(set(label_list))


for i in author_index:
    # 作者top
    if author_list.count(i) > 8:
        author_count.append(author_list.count(i))
        data = {
            'name': i,
            'value': author_list.count(i),
        }
        print(data)

for i in press_index:
    # 出版社top
    if press_list.count(i) > 190:
        press_count.append(press_list.count(i))
        data = {
            'press': i,
            'press_count': press_list.count(i),
        }
        print(data)

def get_author():
    for i in author_index:
        # 作者top
        if author_list.count(i) > 3:
            author_count.append(author_list.count(i))
            data = {
                'name': i,
                'value': author_list.count(i),
            }
            yield (data)



def get_press(types):
    for i in press_index:
        # 出版社top
        if press_list.count(i) > 100:
            press_count.append(press_list.count(i))
            data = {
                'name': i,
                'data': [press_list.count(i)],
                'type': types,
            }
            yield (data)


tag_list = []
tag_index = []
tag_count = []
tag_top = []

def xiaoshuo(num):
    n = num * 100
    n = int(n)
    n = n / 100
    return (n)

def obtain_date(label):
    time1 = 0
    time2 = 0
    time3 = 0
    time4 = 0
    time5 = 0
    time6 = 0
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    for i in all_info.find().limit(10426):
        if i['publish_date'] and i['label']:
            try:
                time = re.findall('(\d\d\d\d)', i['publish_date'])[0]
            except:
                time = 0
            if time != 0:
                if int(time) > 1900 and int(time) < 1989:
                    for tag in i['label']:
                        if tag == label:
                            time1 += 1
                    count1 += 1
                if int(time) > 1990 and int(time) < 1999:
                    for tag in i['label']:
                        if tag == label:
                            time2 += 1
                    count2 += 1
                if int(time) > 2000 and int(time) < 2005:
                    for tag in i['label']:
                        if tag == label:
                            time3 += 1
                    count3 += 1
                if int(time) > 2006 and int(time) < 2010:
                    for tag in i['label']:
                        if tag == label:
                            time4 += 1
                    count4 += 1
                if int(time) > 2011 and int(time) < 2015:
                    for tag in i['label']:
                        if tag == label:
                            time5 += 1
                    count5 += 1
                if int(time) > 2015 and int(time) < 2019:
                    for tag in i['label']:
                        if tag == label:
                            time6 += 1
                    count6 += 1
    data = {
        'tag': [label, time1, time2, time3, time4, time5, time6]
    }
    yield (data)



tag_1 = obtain_date('计算机')
tag_2 = obtain_date('科普')
tag_3 = obtain_date('人工智能')
tag_4 = obtain_date('科学')
tag_5 = obtain_date('编程')
tag_6 = obtain_date('互联网')
print(tag_1)
for i in tag_1:
    print(i['tag'])
    label1 = i['tag']
for i in tag_2:
    print(i['tag'])
    label2 = i['tag']
for i in tag_3:
    print(i['tag'])
    label3 = i['tag']
for i in tag_4:
    print(i['tag'])
    label4 = i['tag']
for i in tag_5:
    print(i['tag'])
    label5 = i['tag']
for i in tag_6:
    print(i['tag'])
    label6 = i['tag']
# charts.plot(series, show='inline', options=dict(title=dict(text='出版社top')))

def index(request):

    info = Modouban.objects[:1]
    press = [data for data in get_press('column')]
    author = [data for data in get_author()]



    limit = 4
    paginatior = Paginator(press,limit)
    page = request.GET.get('page',1)
    loaded = paginatior.page(page)
    context = {
        'title': info,
        'Press_top': press,
        'author_top': author,
        'page': loaded,
        'tag1': label1,
        'tag2': label2,
        'tag3': label3,
        'tag4': label4,
        'tag5': label5,
        'tag6': label6,

    }
    return render(request, 'index.html', context)

def grid(request):

    # author = get_author('column')
    context = {
        'author': author
    }
    return render(request, 'grid_list.html', context)



# def home(request):
#     article = invitation.objects
#
#     page_num = request.GET.get('page',1)
#     loaded = article.page(page_num)
#     context = {
#         'invitation':loaded
#     }
#     return render(request,'home.html',context)