import pymongo
import re
import pandas as pd

client = pymongo.MongoClient('localhost', 27017)
book = client['book']
seek = book['seekY']
old_info = book['computerX']
all_info = book['computerY']
all_info_Z = book['computerZ']
sta = book['statistics']


def update_tag():
    prog_list = []
    java = ['java', 'JAVA', 'Java']
    python = ['python', 'Python', 'PYTHON']
    cc = ['C', 'C++', 'C语言', 'C/C++']
    PHP = ['php', 'PHP', 'WEB', 'web']
    android = ['android', 'Android']
    html = ['WEB', 'web', 'Web']
    tag = 'test'
    for i in all_info.find():
        tag = ''
        if i['label']:
            
            for j in i['label']:
                if j in java:
                    tag = 'Java'
                    break
                if j in cc:
                    tag = 'C/C++'
                    break
                if j in python:
                    tag = 'Python'
                    break
                if j in PHP:
                    tag = 'PHP'
                    break
                if j in android:
                    tag = 'Android'
                    break
                if j in html:
                    tag = 'HTML'
                    break
            if tag != '1':
                all_info.update_many({'_id': i['_id']}, {'$set': {'tag': tag}})
update_tag()


def get_press():
	pipeline = [

	    {'$group': {
		    '_id':"$press",
		    'num_of_tag':{'$sum':1},
		    'score':{'$avg': '$score'},
		    'number':{'$avg': '$number'},
	   	 	}},
	   	{'$project':{'_id':0,'tags':"$_id",'num_of_tag':1, 'score':1, 'number': 1}},
	    {'$match': {
		    "num_of_tag": {'$gte': 150}}
		    },
	    ]

	for i in all_info.aggregate(pipeline):
		# if i['num_of_tag'] > 180:
			print(i)

# get_press()


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

# get_nation()

def get_program():
	pip = [
		{'$group':{
			'_id': '$tag',
			'count': {'$sum': 1},
			'score': {'$avg': '$score'},
			'want': {'$avg': '$read_want'},
			'number': {'$avg': '$number'},
			'read': {'$avg': '$read'},
			}
		},
		{'$project':{'_id':0, 'tags':"$_id", 'count': 1, 'read': 1, 'read_want': 1, 'number': 1, 'score':1, 'want': 1, 'short_number': 1, 'pages': 1, 'program': 1}},
		{'$match': {'count':{'$gte': 10}}}
	
	]
	for i in all_info.aggregate(pip):
		print(i)


get_program()

def update():
	for i in all_info.find():
		# if i['score']:
		# 	pass
		# else:
		# 	i['score'] = 0
		# if i['number'] and i['number'] != '评价人数不足':
		# 	pass
		# else:
		# 	i['number'] = 0
		# all_info_Z.update_many({'_id': i['_id']}, {'$set': {'number': float(i['number'])}})
		# all_info_Z.update_many({'_id': i['_id']}, {'$set': {'score': float(i['score'])}})

		# if i['nation'] == '加拿大':
		# 	all_info.update_many({'_id': i['_id']}, {'$set': {'nation': '加'}})
		# if i['nation'] == '英':
		# 	print(i['author'])

		# if i['read_want']:
		# 	pass
		# else:
		# 	i['read_want'] = 0

		# all_info_Z.update_many({'_id': i['_id']}, {'$set': {'read_want': float(i['read_want'])}})
		# if i['pages']:
		# 	pass
		# else:

		# 	i['pages'] = 0
		# 	if i['pages'] == 'None' or i['pages'] == None:
		# 		i['pages'] = 0

		# all_info.update_many({'_id': i['_id']}, {'$set': {'pages': float(i['pages'])}})
		# if i['price']:
		# 	try:
		# 		i['price'] = re.findall('(\d+)', i['price'])[0]
		# 	except:
		# 		i['price'] = 0
		# else:
		# 	i['price'] = 0

		# all_info_Z.update_many({'_id': i['_id']}, {'$set': {'price': float(i['price'])}})
		# print(i['pages'])
		# if i['nation'] == '中':
		# 	test = re.findall('^[\u4E00-\u9FA5]{2,4}$', i['author'])
		# 	if test:
		# 		pass
		# 	else:
		# 		all_info.update_many({'_id': i['_id']}, {'$set': {'nation': '不明'}})

		# if i['author'] == '不明':
		# 	all_info.update_many({'_id': i['_id']}, {'$set': {'nation': '不明'}})
			# print(i['author'])
		# if i['trans']:
			# print(i['trans'],i['author'],i['nation'])
			# if i['nation'] == '中':
				# print(i['author'])
				# all_info.update_many({'_id': i['_id']}, {'$set': {'nation': '不明'}})
		# if '漫画' in i['label']:
		# 	all_info.delete_one({'title': i['title']})
		# 	print(i['title'])
		if i['program'] == '' or i['program'] == None:
			print(i['title'])
	


# update()


def ref_score():
	for i in all_info.find():
		# print(i['_id'])
		pip = [
			{'$match': {'ISBN':str(i['ISBN'])}}
		]
		for j in old_info.aggregate(pip):
			if j['score']:
				pass
			else:
				j['score'] = 0
			all_info.update({'_id': i['_id']}, {'$set': {'score': float(j['score'])}})
			print(j['score'])
			# print(j)
			# print(j['_id'])

# ref_score()
# for i in all_info.find():
# 	if i['score'] >= 10:
# 		# all_info.update({'_id': i['_id']}, {'$set': {'score': 8.4}})
# 		print(i['score'])

def xiaoshuo(num):
    n = num * 100
    n = int(n)
    n = n / 100
    return n
# -------------------------------------评分详细信息折线图---------------------------------------------------

datas = {

    # 评分
    'score_number': 0,  #
    'score_high': 0,  # 最高评分

    'nine': 1,  # 9分以上
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

def get_score(min, max):

    # 评分
    score_number= 0  #
    score_high= 0  # 最高评分

    nine= 1  # 9分以上
    nine_time= 0  # 9分出版时间
    nine_price= 0  # 9分价钱
    nine_number= 0  # 9分评分人数
    nine_page= 0  # 9分页数
    nine_want= 0  # 九分想读
    nine_read= 0  # 九分读过
    nine_reading= 0  # 九分在读

    nine_shor= 0  # 九分短评
    nine_book= 0  # 九分书评
    nine_note= 0  # 九分笔记


    none_score= 0  # 暂无评分
		
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
            if score >= min and score < max:
                nine += 1
                nine_reading += int(items['reading'])
                nine_read += int(items['read'])
                nine_want += int(items['read_want'])
                nine_book += int(items['book_number'])
                nine_shor += int(items['short_number'])

                nine_note += int(items['note_number'])
                nine_page += int(items['pages'])
                nine_number += int(items['number'])

                try:
                    price = re.findall('(\d\d)', items['price'])[0]
                except:
                    price = 0
                nine_price += int(price)
    scores = {
        'reading': xiaoshuo(nine_reading / nine),
        'read': xiaoshuo(nine_read / nine),
        'want': xiaoshuo(nine_want / nine),
        'number': xiaoshuo(nine_number / nine),

        'book': xiaoshuo(nine_book / nine),
        'short': xiaoshuo(nine_shor / nine),
        'note': xiaoshuo(nine_note / nine),

        'page': xiaoshuo(nine_page / nine),
        
        'price': xiaoshuo(nine_price / nine),
    }
    score_list = [scores['reading'], scores['read'], scores['want'], scores['number'], scores['book'],
                  scores['short'], scores['note'], scores['page'], scores['price']]
    return score_list

# 获取评分对应的详细信息


def get_scores():
    dicts = get_score(0, 4)
    yield dicts
    for i in range(4, 10):
        dicts = get_score(i, i + 1)
        yield dicts


def get_score_index():
    basic_list = ['在读', '已读', '想读', '评分人数', '书评',
                  '短评', '笔记', '页数', '价格']
    score_index = [data for data in get_scores()]
    pd1 = pd.DataFrame(score_index)
    for i in range(0, 9):
        list_ = pd1[i].tolist()
        data = {
            'basic': basic_list[i],
            'data': list_,
        }
        yield data

# score_index = [data for data in get_score_index()]  # 评分对应基本详细信息

# for i in score_index:
# 	print(i)

# def get_score_1():
#     score1_list = []
#     for i in range(0, 4):
#         yield(score_index[i])
# def get_score_2():
#     score1_list = []
#     for i in range(4, 9):
#         yield(score_index[i])
# score1 = [data for data in get_score_1()]
# score2 = [data for data in get_score_2()]

def get_scores0_4():
    for i in range(0, 4, 2):
        dicts = get_score(i, i + 2)
        yield dicts


def get_score_index0_4():
    basic_list = ['在读', '已读', '想读', '评分人数', '书评',
                  '短评', '笔记', '页数', '价格']
    score_index = [data for data in get_scores0_4()]
    pd1 = pd.DataFrame(score_index)
    for i in range(0, 9):
        list_ = pd1[i].tolist()
        data = {
            'basic': basic_list[i],
            'data': list_,
        }
        yield data
# score_index = [data for data in get_score_index0_4()]  # 评分对应基本详细信息

# def get_score_1():
#     score1_list = []
#     for i in range(0, 4):
#         yield(score_index[i])
# def get_score_2():
#     score1_list = []
#     for i in range(4, 9):
#         yield(score_index[i])
# score1 = [data for data in get_score_1()]
# score2 = [data for data in get_score_2()]
# for i in score_index:
# 	print(i)


# for i in all_info.find():
# 	if i['score'] < 4 and i['score'] > 0:
# 		print(i['title'])