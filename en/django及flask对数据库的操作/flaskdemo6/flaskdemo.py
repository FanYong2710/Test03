#coding = utf-8
'''
    @name:flask 数据库操作
    @function:
    @author:Mr.Zheng
    @date:'2018-12-13 11:38'
'''
from flask import Flask,render_template,redirect,request,url_for
from settings import config
app = Flask(__name__)
app.config.from_object(config["db"])

# 步骤2：创建sqlalchemy对象
# 导入sqlalchemy 模块
from flask_sqlalchemy import SQLAlchemy
# 创建数据操作对象
db = SQLAlchemy(app)

# 步骤3：建立模型生成数据表
# 自定义类继承db.Model
class Roles(db.Model):
    # 设置数据表名
    __tablename__ = "Roles"
    # 设置数据表字段
    rid = db.Column(db.Integer,primary_key=True)
    rname = db.Column(db.String(20))
    # 构造方法
    def __init__(self,rname):
        self.rname = rname
    # 创建对象的输出方法（测试用类似于str）
    def __repr__(self):
        return "Roles[id = {0},name = {1}]".format(self.rid,self.rname)

@app.route("/index/")
def index():
    return render_template("index.html")
# 创建数据表
@app.route("/createRoles/")
def createRoles():
    # 删除数据表
    db.drop_all()
    print(">>数据表已清除")
    #创建新表
    db.create_all()
    print(">>数据表创建成功")
    return render_template("index.html",msg="数据表创建成功")

# 添加业务
@app.route("/addRoles/",methods=["GET","POST"])
def addRoles():
    if request.method == "POST":
        # 接收数据
        rname = request.values.get("rname")
        # 创建模型对象并初始化
        roles = Roles(rname)
        # 写入数据表
        db.session.add(roles)
        # 事务提交
        db.session.commit()
        return redirect(url_for("queryAll"))
    else:
        return render_template("addRoles.html")


# 查询业务
@app.route("/showAll/")
def queryAll():
    # 查询数据
    rolesall = db.session.query(Roles).all()
    return render_template("show.html",roleall = rolesall)

# 删除业务
@app.route("/delRoles/<int:id>/")
def delRoles(id):
    #根据指定条件查询并删除数据
    db.session.query(Roles).filter_by(rid=id).delete()
    #提交事务
    db.session.commit()
    return redirect(url_for("queryAll"))

#修改业务
@app.route("/updateRoles/<int:id>/",methods=["GET","POST"])
def updateRoles(id):
    if request.method == "POST":
        # 接收请求参数
        rname = request.values.get("rname")
        # 组合字典
        data = {}
        data["rname"] = rname
        # 修改
        db.session.query(Roles).filter_by(rid=id).update(data)
        db.session.commit()
        return redirect(url_for("queryAll"))
    else:
        # 根据id查询对象
        roles = db.session.query(Roles).filter_by(rid=id).first()
        return render_template("updateRoles.html",roles=roles)

if __name__ == '__main__':
    app.run()
    pass