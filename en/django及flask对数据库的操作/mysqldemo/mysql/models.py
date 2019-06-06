from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=30)