from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator # 分页
# Create your views here.
from learn.models import Modouban




def home(request):

    info = Modouban.objects[:1]

    context = {
        'title':info[0].title
    }
    return render(request, 'list.html', context)

# def home(request):
#     article = invitation.objects
#
#     page_num = request.GET.get('page',1)
#     loaded = article.page(page_num)
#     context = {
#         'invitation':loaded
#     }
#     return render(request,'home.html',context)