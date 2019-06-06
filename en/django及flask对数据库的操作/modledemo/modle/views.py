from django.shortcuts import render
from modle.models import Book
from django.http import HttpResponse
# Create your views here.
def goindex(request):
    return render(request,"index.html")

# 添加数据业务
def addBook(request):
    if request.POST:
        # 接收数据
        name = request.POST.get("bname")
        # 写入数据库
        book = Book(bname=name)
        book.save()
        return HttpResponse("<script>alert('添加成功')</script>")
    else:
        return render(request,"insert.html")

# 查询业务
def queryBook(request):
    #查询数据
    result = Book.objects.all()
    # print(type(result),result)
    # return HttpResponse(result)
    content = {}
    content["bookList"] = result
    return render(request,"show.html",content)

# 根据指定字段查询数据
# 根据编号查询
def queryBookById(request):
    # 接收数据
    id = request.GET.get("id")
    #查询数据
    result = Book.objects.get(bid=id)
    # print(result)
    # return HttpResponse()
    content = {}
    content["book"] = result
    return render(request,"showId.html",content)

# 删除业务(根据条件)
def deleteBook(request,id):
    # 删除数据
    Book.objects.filter(bid=id).delete()
    return HttpResponse("<script>alert('删除成功')</script>")

# 修改业务
def updateBookById(request,id,name):
    # 修改数据
    Book.objects.filter(bid=id).update(bname=name)
    return HttpResponse("<script>alert('修改成功')</script>")
# get和filter
def getTest(request):
    res = Book.objects.get(bname="程序设计")
    return render(request,"getandfilter.html",{"gettest":res})

def getFilter(request):
    res = Book.objects.filter(bname="p")
    print(res)
    return render(request,"getandfilter.html",{"filtertest":res})
# model中使用 sql语句
def SqlTest(request):
    # raw --- 执行sql语句
    # res = Book.objects.raw("select * from modle_book where bname='python'")
    res = Book.objects.raw("select * from modle_book where bname=%s",params=["python"])
    # extra -- 执行sql
    # res = Book.objects.all().extra(where=["bname='python'"])
    print(res)
    return render(request,"rawshow.html",{"data":res})
