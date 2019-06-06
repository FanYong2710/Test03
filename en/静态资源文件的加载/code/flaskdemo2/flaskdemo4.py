#coding = utf-8

'''
flask  session
'''
import os

from flask import Flask,render_template,session
app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/session/")
def sessionmesage():
    return render_template("session.html")

# 设置session
@app.route("/setSession/")
def setSession():
    print(os.urandom(24))
    # 设置session
    session["sessiontest"] = "123"
    return "session设置成功"

# 获取session
@app.route("/getSession/")
def getSession():
    # return session["sessiontest"]
    return session.get("sessiontest")
if __name__ == '__main__':
    app.run()