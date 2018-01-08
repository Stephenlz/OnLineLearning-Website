from django.db import models
from datetime import datetime


# 城市信息
class CityDict(models.Model):
    name = models.CharField(max_length=100, verbose_name="cityName")
    desc = models.CharField(max_length=200, verbose_name="description")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "CityDict"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程机构
class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name="orgName")
    desc = models.TextField(verbose_name="description")
    category = models.CharField(max_length=20, default='company',
                                choices=(('company', 'company'), ('univeristy', 'univeristy')), verbose_name='category')
    clickNum = models.IntegerField(default=0, verbose_name="clickNum")
    address = models.CharField(max_length=150, verbose_name="address")
    favoriteNum = models.IntegerField(default=0, verbose_name="favoriteNum")
    addTime = models.DateTimeField(default=datetime.now)
    studentNum = models.IntegerField(default=0, verbose_name="studentNum")
    courseNum = models.IntegerField(default=0, verbose_name="courseNum")
    image = models.ImageField(upload_to="organization/%Y/%m", verbose_name="pageImage")
    city = models.ForeignKey(CityDict, verbose_name="city")

    class Meta:
        verbose_name = "CourseOrg"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 教师资料
class Teacher(models.Model):
    name = models.CharField(max_length=100, verbose_name="teacherName")
    workYears = models.IntegerField(default=0, verbose_name="workYears")
    workCompany = models.CharField(max_length=50, verbose_name="workCompany")
    level = models.CharField(max_length=50, verbose_name="level")
    features = models.CharField(max_length=100, verbose_name="features")
    favoriteNum = models.IntegerField(default=0, verbose_name="favoriteNum")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")
    organization = models.ForeignKey(CourseOrg, verbose_name="courseOrg")
    photo = models.ImageField(upload_to="teacher/%Y/%m", verbose_name='photo', max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
