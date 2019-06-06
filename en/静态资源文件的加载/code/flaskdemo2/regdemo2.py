#coding = utf-8

'''
用户注册
'''
from flask import Flask,request,Response,make_response
app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>注册</title>
</head>
<body>
<form method="post" action="/reg2/">
   用户名： <input type="text" name="user"><br/>
    密码：<input type="password" name="pass"><br/>
    爱好：<input type="checkbox" name="hobby" value="吃饭">吃饭
    <input type="checkbox" name="hobby" value="睡觉">睡觉
    <input type="checkbox" name="hobby" value="打豆豆">打豆豆<br/>
    <input type="submit" value="注册">
</form>
</body>
</html>
'''

@app.route("/reg2/",methods=["GET","POST"])
def reg():
    if request.method == "POST":
        user = request.values.get("user")
        pwd = request.values.get("pass")
        hobby = request.values.getlist("hobby")
        message = "用户名：{0}<br/>密码：{1}<br/>爱好：{2}".format(user,pwd,hobby)
        return message
    else:
        return html

if __name__ == '__main__':
    app.run()