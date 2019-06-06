#coding = utf-8
from flask import Flask,request,Response
app = Flask(__name__)
app.config["DEBUG"] = True

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
</head>
<body>
<form method="post" action="/login/">
   用户名： <input type="text" name="user" value="{0}"><br/>
    密码：<input type="password" name="pass"><br/>
    <input type="submit" value="登录">
</form>
</body>
</html>
'''
@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "POST":
        # 接收用户名密码
        user = request.values.get("user")
        pwd = request.values.get("pass")
        # 默认 admin
        if user == "admin" and pwd == "admin":
            # 设置cookie
            response = Response("欢迎您：{0}".format(user))
            response.set_cookie("username",user)
            return response
        else:
            # 获取cookie
            username = request.cookies.get("username")
            if username == None:
                username = ""
            return html.format(username)
        pass
    else:
        # 获取cookie
        username = request.cookies.get("username")
        if username == None:
            username = ""
        return html.format(username)


if __name__ == '__main__':
    app.run()