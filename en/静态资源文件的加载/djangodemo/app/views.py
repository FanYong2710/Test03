from django.shortcuts import render

# Create your views here.
# 视图控制器函数
def goindex(request):
    return render(request,"index.html")

# 添加test页面
def gotest(request):
    return render(request,"test.html")