from django.shortcuts import render
from django.http import HttpResponseRedirect
from learn.models import douban
from django.core.paginator import Paginator # 分页
# Create your views here.
from learn.models import douban



def home(request):
    test = douban.objects[:1]

    context = {
        '标签':test[0].标签,
    }
    return render(request, 'list.html',context)

# def home(request):
#     article = invitation.objects
#
#     page_num = request.GET.get('page',1)
#     loaded = article.page(page_num)
#     context = {
#         'invitation':loaded
#     }
#     return render(request,'home.html',context)