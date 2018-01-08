from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime


# 用户资料
class UserProfile(AbstractUser):
    nickName = models.CharField(max_length=50, verbose_name='nickname', default="")
    birthDay = models.DateField(verbose_name='birthday', null=True, blank=True)
    gender = models.CharField(max_length=5, choices=(('male', "man"), ('female', "woman")), default='male')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, null=True)
    image = models.ImageField(upload_to="image/%Y/%m", default='image/default.png', max_length=100)

    class Meta:
        verbose_name = "user_Information"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 邮箱认证
class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='verifyCode')
    email = models.EmailField(max_length=50, verbose_name="emailBox")
    sendType = models.CharField(choices=(('register', 'register'), ('forget', 'forget')), max_length=10)
    sendTime = models.DateTimeField(default=datetime.now, verbose_name="sendTime")

    class Meta:
        verbose_name = "EmailVerifyCode"
        verbose_name_plural = verbose_name


# 轮播图
class PageBanner(models.Model):
    title = models.CharField(max_length=100, verbose_name="title")
    image = models.ImageField(max_length=100, upload_to="banner/%Y/%m", verbose_name="image")
    url = models.URLField(max_length=200, verbose_name="url")
    index = models.IntegerField(default=100, verbose_name="index")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "PageBanner"
        verbose_name_plural = verbose_name
