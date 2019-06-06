#coding = utf-8

'''
用户注册
'''
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/reg/",methods=["GET","POST"])
def reg():
    if request.method == "POST":
        user = request.values.get("user")
        pwd = request.values.get("pass")
        hobby = request.values.getlist("hobby")
        message = "用户名：{0}<br/>密码：{1}<br/>爱好：{2}".format(user,pwd,hobby)
        return message
    else:
        return render_template("reg.html")

if __name__ == '__main__':
    app.run()