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



for i in all_info.find():
	rank = 0
	sign = 0
	if i['number'] and i['number'] != '评分人数不足':
		if i['label']:
			for j in i['label']:
				if j in "小说科普心理散文随笔生活商业青春自然艺术哲学爱情文学财富理财经济管理心理心理学成长漫画文化传媒娱乐奇幻旅行生活励志传记历史伦理医学健身育儿数学社会":
					sign = 1
		if sign == 0:
			if i['score']:
				rank = int(i['number']) * float(i['score'])
				print(rank)

	all_info.update_many({'_id': i['_id']}, {'$set': {'rank': rank}})

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








    class RotateUserAgentMiddleware(UserAgentMiddleware):
    def __int__(self, user_agent=''):
        self.user_agent = user_agent

    def process_request(self, request, spider):
        ua = random.choice(self.user_agent_list)
        if ua:
            logging.info(ua)
            request.headers.setdefault('User-Agent', ua)
    user_agent_list = [
        # user-agent列表信息
    ]


        DOWNLOADER_MIDDLEWARES = {
            'books.middlewares.RotateUserAgentMiddleware': 125, 
        }



            try:
                item['price'] = re.findall(r'定价:</span>(\d*.\d*)', base_info)[0]
            except:
                item['price'] = None


            client = pymongo.MongoClient('localhost', 27017)
            book = client['book']
            all = book['computerY']

            try:
                nation = re.findall('\[(.*?)\]|\((.*?)\)|\【(.*?)\】|\（(.*?)\）', items['author'])[0] 
            except:
                nation = ['不明']
            all.update_many({'_id': items['_id']}, {'$set': {'nation': nation}})



            for j in old_info.find():
                if j['score']:
                    pass
                else:
                    j['score'] = 0
                all_info.update({'_id': i['_id']}, {'$set': {'score': float(j['score'])}})


def get_nation():
    pip = [
        {'$group':{
            '_id': '$nation',
            'count': {'$sum': 1},
            'score': {'$avg': '$score'},
            'want': {'$avg': '$read_want'},
            'number': {'$avg': '$number'},
            'read': {'$avg': '$read'},
            }
        },
        {'$match':{
            'count': {'$gte': 100}
            },
        }
    ]
    for i in all_info.aggregate(pip):
        print(i)
