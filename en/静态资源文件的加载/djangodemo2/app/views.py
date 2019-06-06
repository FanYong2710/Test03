from django.shortcuts import render

# Create your views here.
def goindex(req):
    return render(req,"index.html")

def gologin(request):
    return render(request,"login.html")

def goreg(request):
    return render(request,"reg.html")
# 视图控制器函数接收请求
def test(request):
    # 1.接收客户端请求（get）
    res = request.GET.get("a")
    # 2.处理请求
    print(res)
    # 3.响应
    return render(request,"index.html")