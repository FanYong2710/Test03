from django.db import models

# Create your models here.
# 继承models
class Book(models.Model):
    # 设置数据表字段
    bid = models.AutoField(primary_key=True)
    bname = models.CharField(max_length=30)