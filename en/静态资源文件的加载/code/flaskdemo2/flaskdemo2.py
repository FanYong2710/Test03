#coding = utf-8
'''
url 地址反转
'''

from flask import Flask,url_for,redirect
app = Flask(__name__)

@app.route("/show/")
def goindex():
    return "index"

@app.route("/geturl/")
def geturl():
    # return url_for("goindex")
    return redirect(url_for("goindex"))

if __name__ == '__main__':
    app.run()