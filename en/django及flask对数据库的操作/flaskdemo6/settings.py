#coding = utf-8
class DataBaseSetting:
    DEBUG = True
    # 数据连接
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

config = {
    "db":DataBaseSetting
}
