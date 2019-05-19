from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator # 分页
# Create your views here.
from learn.models import Modouban
import pymongo
import charts

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
            'author': i,
            'author_count': author_list.count(i),
        }
        print(data)

for i in press_index:
    # 出版社top
    if press_list.count(i) > 100:
        press_count.append(press_list.count(i))
        data = {
            'press': i,
            'press_count': press_list.count(i),
        }
        print(data)

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

series = [data for data in get_press('column')]
charts.plot(series, show='inline', options=dict(title=dict(text='出版社top')))

def index(request):

    info = Modouban.objects[:1]
    press = [data for data in get_press('column')]
    limit = 4
    paginatior = Paginator(press,limit)
    page = request.get.GET('page',1)
    loaded = paginatior.page(page)
    context = {
        'title': info,
        'Press_top':loaded,
    }
    return render(request, 'list.html', context)

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