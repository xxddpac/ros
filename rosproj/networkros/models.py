from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(verbose_name="用户名", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=50)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(verbose_name="操作时间", auto_now_add=True)

    class Meta:
        verbose_name = "用户名密码后台验证"
        verbose_name_plural = verbose_name
        db_table = "user"



class DeviceManage(models.Model):
    owner = models.CharField(verbose_name="设备归属者", max_length=50)
    address = models.CharField(verbose_name="设备管理地址", max_length=50)
    update_time = models.DateTimeField(verbose_name="更新时间", auto_now=True)
    create_time = models.DateTimeField(verbose_name="操作时间", auto_now_add=True)

    class Meta:
        verbose_name = "用户设备对应关系"
        verbose_name_plural = verbose_name
        db_table = "DeviceManage"