from django.db import models

# Create your models here.
from mongoengine import *
from mongoengine import connect
# Create your models here.

# 指明要连接的数据库
connect('book', host='127.0.0.1', port=27017)

class Modouban(Document):
    # 定义数据库中的所有字段
    # 基本信息
    info = StringField()

    # 书名
    title = StringField()

    # 作者
    author = StringField()

    # 出版社
    press = StringField()

    # 译者
    trans = StringField()

    # 出版年
    publish_date = StringField()

    # 页数
    pages = StringField()

    # 定价
    price = StringField()

    # 电商价
    price_d = StringField()

    # 标签
    label = ListField(StringField())

    # ISBN
    ISBN = StringField()

    # 读过的人
    read = StringField()

    # 想读的人
    read_want = StringField()

    # 在读的人
    reading = StringField()

    # 评分
    score = ListField(StringField())

    # 评分人数
    number = StringField()

    # 图书链接
    url = StringField()

    # 作者简介
    # author_s = StringField()

    # 内容简介
    # summary = StringField()

    # 读过、想读、在读
    # read_box = StringField()

    # 图片链接
    image = StringField()

    # 一星
    one = StringField()

    # 二星
    two = StringField()

    # 三星
    three = StringField()

    # 四星
    four = StringField()

    # 五星
    five = StringField()

    # 短评
    short = StringField()

    # 短评数量
    short_number = StringField()

    # 书评数量
    book_number = StringField()

    # 笔记数量
    note_number = StringField()

    nation = StringField()

    rank = StringField()

    # 指明连接的数据表名
    meta = {'collection': 'computerZ'}



# 测试是否连接成功
for i in Modouban.objects[:100]:  # [:10] 分片
    print(i.author)