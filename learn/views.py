from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator  # 分页
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

# 所有数据
author_list = []
press_list = []
label_list = []

# 统计类
datas = {

    # 评分
    'score_number': 0,  #
    'score_high': 0,  # 最高评分
    ''

    'nine': 0,  # 9分以上
    'nine_time': 0,  # 9分出版时间
    'nine_price': 0,  # 9分价钱
    'nine_number': 0,  # 9分评分人数
    'nine_page': 0,  # 9分页数
    'nine_want': 0,  # 九分想读
    'nine_read': 0,  # 九分读过
    'nine_reading': 0,  # 九分在读

    'nine_shor': 0,  # 九分短评
    'nine_book': 0,  # 九分书评
    'nine_note': 0,  # 九分笔记


    'none_score': 0,  # 暂无评分
}


def cleanDb():
    # 清洗数据库
    for i in all_info.find():

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
            update_tag = i['label']
            for tag in i['label']:
                label_list.append(tag)
                # 更新数据
                # if tag == '数据分析' or tag == '机器学习':
                #     update_tag.append('人工智能')
                #
                # if tag == '计算机':
                #     update_tag.append('计算机科学')
                # if tag in 'javaJavaJAVAcc++CC++PythonpythonandroidAndroidHTML5C语言C#Spring' and '编程' not in update_tag:
                #     update_tag.append('编程')
                # if tag == 'sql' or tag == 'oracle' or tag in 'sql数据库SQLMysqlmysql':
                #     update_tag.append('数据库')
                # if tag == 'java':
                #     update_tag.append('Java')
                # if tag == 'python':
                #     update_tag.append('Python')
                # if tag in 'cCc++C++':
                #     update_tag.append('C')

        author_list.append(i['author'])
        press_list.append(i['press'])

        # print(update_tag)
        # 更新数据
        # all_info.update_many({'_id': i['_id']}, {'$set': {'author': author}})
        # all_info.update_many({'_id': i['_id']}, {'$set': {'press': press}})
        # all_info.update_many({'_id': i['_id']}, {'$set': {'label': update_tag}})


cleanDb()

# 不重复数据
author_index = []
press_index = []
label_index = []

# 出现次数
author_count = []
press_count = []
label_count = []

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
            if i != '不明' and i != '[日]藤子不二雄Ⓐ' and i != '[英]史蒂芬·霍金' and i != '刘慈欣' and i != '吴军' and i != '[美]阿尔伯特·爱因斯坦':
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
    return n


def obtain_date(label):
    time1 = 0
    time2 = 0
    time3 = 0
    time4 = 0
    time5 = 0
    time6 = 0
    rest_list = ['其他', 0, 0, 0, 0, 0, 0]
    for i in all_info.find():
        if i['publish_date'] and i['label']:
            try:
                time = re.findall('(\d\d\d\d)', i['publish_date'])[0]
            except:
                time = 0
            if time != 0:
                if int(time) > 1900 and int(time) < 1989:
                    for tag in i['label']:
                        if tag == label or label in tag:
                            time1 += 1
                    rest_list[1] += 1
                if int(time) > 1990 and int(time) < 1999:
                    for tag in i['label']:
                        if tag == label or label in tag:
                            time2 += 1
                    rest_list[2] += 1
                if int(time) > 2000 and int(time) < 2005:
                    for tag in i['label']:
                        if tag == label or label in tag:
                            time3 += 1
                    rest_list[3] += 1
                if int(time) > 2006 and int(time) < 2010:
                    for tag in i['label']:
                        if tag == label or label in tag:
                            time4 += 1
                    rest_list[4] += 1
                if int(time) > 2011 and int(time) < 2015:
                    for tag in i['label']:
                        if tag == label or label in tag:
                            time5 += 1
                    rest_list[5] += 1
                if int(time) > 2015 and int(time) < 2019:
                    for tag in i['label']:
                        if tag == label or label in tag:
                            time6 += 1
                    rest_list[6] += 1
    data = {
        'time': [label, time1, time2, time3, time4, time5, time6],
        'all_count': rest_list,
    }
    yield data


def obtain_prog(label):
    pro_list = [0, 0, 0]
    for i in seek.find():
        if i['publish_date'] and i['label'] and i['tag']:
            try:
                time = re.findall('(\d\d\d\d)', i['publish_date'])[0]
            except:
                time = 0
            if time != 0 and i['tag'] == label:

                # if int(time) > 1900 and int(time) < 1999:
                #     pro_list[0] += 1
                if int(time) > 2000 and int(time) < 2009:
                    pro_list[0] += 1
                if int(time) > 2010 and int(time) < 2014:
                    pro_list[1] += 1
                if int(time) > 2015 and int(time) < 2019:
                    pro_list[2] += 1
    data = {
        'name': label,
        'data': pro_list,
    }
    return data


def get_pro():
    yield obtain_prog('python')
    yield obtain_prog('java')
    yield obtain_prog('c++')


# 获取编程历年信息
prog = [data for data in get_pro()]


tag_1 = obtain_date('计算机科学')
tag_2 = obtain_date('机器学习')
tag_3 = obtain_date('数据库')
tag_7 = obtain_date('人工智能')
tag_4 = obtain_date('设计')
tag_5 = obtain_date('编程')
tag_6 = obtain_date('互联网')
tag_8 = obtain_date('Python')
tag_9 = obtain_date('Java')
tag_10 = obtain_date('C')


for i in tag_1:
    label1 = i['time']
for i in tag_2:
    label2 = i['time']
for i in tag_3:
    label3 = i['time']
for i in tag_4:
    label4 = i['time']
for i in tag_5:
    label5 = i['time']
for i in tag_6:
    label6 = i['time']
    res = i['all_count']
for i in tag_7:
    label7 = i['time']
lab = {
    'l1': label1,
    'l2': label2,
    'l3': label3,
    'l7': label7,
    'l4': label4,
    'l5': label5,
    'l6': label6,
}
pd1 = pd.DataFrame(lab)
# pd1.loc['Row_sum'] = pd1.apply(lambda x: x.sum()) #行
pd1['Col_sum'] = pd1.apply(lambda x: x.sum(), axis=1)
pd1['Col_sum'][0] = 0
pds2 = pd.Series(res)
pds2[0] = 0
res = pds2 - pd1['Col_sum']

res = pd.Series.tolist(res)  # 其他标签list

print(pd1)


# p2_x3 评分详细信息折线图
def get_score(min, max):
    for items in all_info.find():
        # 将没有评分的重置为0
        if items['score']:
            pass
        else:
            items['score'] = 0
        if items['number']:
            pass
        else:
            items['number'] = 0
        if items['number'] == '评分人数不足':
            items['number'] = 0
        if items['pages']:
            # 评分分级
            score = float(items['score'])
            if score > min and score < max:
                datas['nine'] += 1
                datas['nine_reading'] += int(items['reading'])
                datas['nine_read'] += int(items['read'])
                datas['nine_want'] += int(items['read_want'])
                datas['nine_book'] += int(items['book_number'])
                datas['nine_shor'] += int(items['short_number'])

                datas['nine_note'] += int(items['note_number'])
                datas['nine_page'] += int(items['pages'])
                datas['nine_number'] += int(items['number'])

                try:
                    price = re.findall('(\d\d)', items['price'])[0]
                except:
                    price = 0
                datas['nine_price'] += int(price)
    scores = {
        'reading': xiaoshuo(datas['nine_reading'] / datas['nine']),
        'read': xiaoshuo(datas['nine_read'] / datas['nine']),
        'want': xiaoshuo(datas['nine_want'] / datas['nine']),

        'book': xiaoshuo(datas['nine_book'] / datas['nine']),
        'short': xiaoshuo(datas['nine_shor'] / datas['nine']),
        'note': xiaoshuo(datas['nine_note'] / datas['nine']),

        'page': xiaoshuo(datas['nine_page'] / datas['nine']),
        'number': xiaoshuo(datas['nine_number'] / datas['nine']),
        'price': xiaoshuo(datas['nine_price'] / datas['nine']),
    }
    score_list = [scores['reading'], scores['read'], scores['want'], scores['book'],
                  scores['short'], scores['note'], scores['page'], scores['number'], scores['price']]
    return score_list

# 获取评分对应的详细信息


def get_scores():
    dicts = get_score(0, 4)
    yield dicts
    for i in range(4, 10):
        dicts = get_score(i, i + 1)
        yield dicts


def get_score_index():
    basic_list = ['reading', 'read', 'want', 'book',
                  'short', 'note', 'page', 'number', 'price']
    score_index = [data for data in get_scores()]
    pd1 = pd.DataFrame(score_index)
    for i in range(0, 9):
        list_ = pd1[i].tolist()
        data = {
            'name': basic_list[i],
            'data': list_,
        }
        yield data


score_index = [data for data in get_score_index()]  # 评分对应基本详细信息
print(score_index)


def index(request):

    info = Modouban.objects[:1]
    press = [data for data in get_press('column')]
    author = [data for data in get_author()]

    limit = 4
    paginatior = Paginator(info, limit)
    page = request.GET.get('page', 1)
    loaded = paginatior.page(page)
    context = {
        'for': [0, 1, 2, 3, 4, 5, 6],
        'all_info': loaded,
        'Press_top': press,
        'author_top': author,
        'tag1': label1,
        'tag2': label2,
        'tag3': label3,
        'tag4': label4,
        'tag5': label5,
        'tag6': label6,
        'tag7': label7,
        'res': res,  # 其他标签
        'prog': prog,  # 编程语言柱状图
        'score_index': score_index,  # 评分详细信息

    }
    return render(request, 'index.html', context)


# def home(request):
#     article = invitation.objects
#
#     page_num = request.GET.get('page',1)
#     loaded = article.page(page_num)
#     context = {
#         'invitation':loaded
#     }
#     return render(request,'home.html',context)
