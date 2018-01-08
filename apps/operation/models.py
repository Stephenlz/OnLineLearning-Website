from datetime import datetime
from django.db import models
from users.models import UserProfile
from courses.models import Course


# 用户咨询
class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name="name")
    mobile = models.CharField(max_length=11, verbose_name="mobile")
    courseName = models.CharField(max_length=50, verbose_name="courseName")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "UserAsk"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 用户评论
class CourseComments(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="user")
    course = models.ForeignKey(Course, verbose_name="course")
    comments = models.CharField(max_length=200, verbose_name="comments")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "CourseComments"
        verbose_name_plural = verbose_name


# 用户收藏
class UserFavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="user")
    dataId = models.IntegerField(default=0, verbose_name="dataId")
    dataType = models.IntegerField(choices=((1, "class"), (2, "courseOrganization"), (3, "teacher")), default=1,
                                   verbose_name="dataType")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "UserFavorite"
        verbose_name_plural = verbose_name


# 用户消息
class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name="userId")
    message = models.CharField(max_length=500, verbose_name="message")
    hasRead = models.BooleanField(default=False, verbose_name="hasRead")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "UserMessage"
        verbose_name_plural = verbose_name


# 用户课程
class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name="user")
    course = models.ForeignKey(Course, verbose_name="course")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "UserCourse"
        verbose_name_plural = verbose_name


