from django.db import models

# Create your models here.
from mongoengine import *

# Create your models here.

# 指明要连接的数据库
connect('book',host = '127.0.0.1',port = 27017)

class douban(Document):
    # 定义数据库中的所有字段
    作者 = StringField()
    评分 = StringField()
    评分人数 = StringField()
    定价 = StringField()
    想读的人=StringField()
    书名=StringField()
    ISBN =StringField()
    页数 = StringField()
    标签 = StringField()
    在读的人 = StringField()
    作者简介 =StringField()
    出版社 = StringField()
    图书链接 = StringField()
    出版年 = StringField()
    读过的人 = StringField()
    内容简介 = StringField()

    # 指明连接的数据表名
    meta = {'collection':'douban'}


# 测试是否连接成功
for i in douban.objects[:10]:
    print(i.标签[1])
