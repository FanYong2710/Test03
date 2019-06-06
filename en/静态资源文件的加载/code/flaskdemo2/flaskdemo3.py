#coding = utf-8
'''
cookie
设置
'''

from flask import Flask,render_template,Response,request
app = Flask(__name__)

@app.route("/cookie/")
def cookie():
    return render_template("cookie.html")

# 设置cookie
@app.route("/setCookie/")
def setCookie():
    #获取响应对象
    response = Response("cookie设置成功")
    # 设置cookie
    response.set_cookie("cooktest","123",max_age=3600)
    # 响应客户端
    return response

@app.route("/getCookie/")
def getCookie():
     # 获取cookie
     cookie = request.cookies.get("cooktest")
     return cookie

@app.route("/delCookie/")
def delCookie():
    # 删除cookie
    respnose = Response("cookie删除成功")
    respnose.delete_cookie("cooktest")
    return respnose

if __name__ == '__main__':
    app.run()