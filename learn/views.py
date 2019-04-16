from django.shortcuts import render
from django.http import HttpResponseRedirect
from learn.models import douban
from django.core.paginator import Paginator # 分页
# Create your views here.



def home(request):
    return render(request, 'list.html')

# def home(request):
#     article = invitation.objects
#
#     page_num = request.GET.get('page',1)
#     loaded = article.page(page_num)
#     context = {
#         'invitation':loaded
#     }
#     return render(request,'home.html',context)