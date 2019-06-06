#coding = utf-8
'''
    @name:文件上传(参数配置)(图片回显)
    @function:
    @author:Mr.Zheng
    @date:'2018-12-12 14:52'
'''
import os
import uuid
from settings import config
from flask import Flask,render_template,request,url_for
from werkzeug.utils import secure_filename
app = Flask(__name__)
# 导入配置信息
app.config.from_object(config["fileupload"])
# 获取数据
upload_foloder = app.config["UPLOAD_FOLODER"]
allowed_extnions = app.config["ALLOWED_EXTENIONS"]

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
        # 文件类型验证
        if filetype in allowed_extnions:
            # 设置文件夹路径
            uploadpath = os.getcwd() + os.sep + upload_foloder
            # 服务器路径地址
            if not os.path.exists(uploadpath):
                os.mkdir(uploadpath)
            # print(uploadpath)
            # 写入服务器
            # file.save(uploadpath+os.sep+filename)
            # 处理文件名
            filename = str(uuid.uuid1())+"."+filetype
            # filename = secure_filename(filename)
            file.save(uploadpath + os.sep + filename)
            # 获取文件的url
            url = url_for("static",filename="file/"+filename)
            print(url)
            return render_template("fileupload.html",msg="文件上传成功",url=url)
        else:
            return render_template("fileupload.html", msg="文件类型不符")
    else:
        return render_template("fileupload.html")

if __name__ == '__main__':
    app.run()
    pass