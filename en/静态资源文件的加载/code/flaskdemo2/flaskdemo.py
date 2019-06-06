#coding = utf-8
'''
flask 加载静态资源文件

'''

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/index/")
def index():
    return render_template("index.html",msg="zhangsan")

@app.route("/test/")
def test():
    list = ["苹果","香蕉","橘子"]
    return render_template("index.html",data=list)

if __name__ == '__main__':
    app.run()