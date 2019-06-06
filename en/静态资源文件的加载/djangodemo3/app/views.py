from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def goindex(request):
    return render(request,"index.html")

def goadd(request):
    return render(request,"add.html")

# 接收客户端请求数据
def getData(request):
    res = request.GET.get("wd")
    print(res)
    # 响应对象
    return HttpResponse("<script>alert('{0}');</script>".format(res))

# 计算两个数的和
def calc(request):
    # 接收请求
    num1 = request.GET.get("num1")
    num2 = request.GET.get("num2")
    #处理请求
    result = int(num1) + int(num2)
    #响应客户端
    return HttpResponse(result)
