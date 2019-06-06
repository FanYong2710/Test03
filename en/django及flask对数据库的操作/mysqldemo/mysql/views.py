from django.shortcuts import render
from mysql.models import Dept
from django.http import HttpResponse

# Create your views here.
def test(request):
    Dept.objects.create(dname="zhangsan")
    return HttpResponse("数据写入成功")