#coding = utf-8
'''
    @name:文件上传
    @function:
    @author:Mr.Zheng
    @date:'2018-12-12 14:52'
'''
import os
import uuid
from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/index/")
def index():
    return render_template("index.html")

# 文件上传业务
@app.route("/fileupload/",methods=["GET","POST"])
def fileupload():
    if request.method == "POST":
        # 获取文件对象
        file = request.files["file"]
        # 获取文件名
        filename = file.filename
        filetype = filename.split(".")[-1]
        print("文件信息：")
        print("文件名称:{0}".format(filename))
        print("文件类型:{0}".format(filetype))
        # 设置文件夹路径
        uploadpath = os.getcwd() + os.sep + "static/file"
        # 服务器路径地址
        if not os.path.exists(uploadpath):
            os.mkdir(uploadpath)
        # print(uploadpath)
        # 写入服务器
        # file.save(uploadpath+os.sep+filename)
        # 处理文件名
        filename = str(uuid.uuid1())+"."+filetype
        file.save(uploadpath + os.sep + filename)
        return "文件上传成功"
    else:
        return render_template("fileupload.html")

if __name__ == '__main__':
    app.run()
    pass