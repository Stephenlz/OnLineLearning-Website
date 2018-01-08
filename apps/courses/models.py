from django.db import models
from datetime import datetime
from organization.models import CourseOrg


# 课程基本信息
class Course(models.Model):
    CourseOrg = models.ForeignKey(CourseOrg, verbose_name='courseOrg', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name="courseName")
    desc = models.CharField(max_length=300, verbose_name="description")
    detail = models.TextField(verbose_name="courseDetail")
    degree = models.CharField(max_length=20,
                              choices=(('primary', 'primary'), ('middle', 'middle'), ('senior', 'senior')),
                              default='primary',
                              verbose_name="degree")
    learnTime = models.IntegerField(default=0, verbose_name="learnTime")
    studentNum = models.IntegerField(default=0, verbose_name="studentNum")
    favoriteNum = models.IntegerField(default=0, verbose_name="favoriteNum")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name="pageImage")
    clickNum = models.IntegerField(default=0, verbose_name="clickNum")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "course"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 章节
class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name="course")
    name = models.CharField(max_length=50, verbose_name="LessonName")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 视频
class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name="lesson")
    name = models.CharField(max_length=50, verbose_name="VideoName")
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "Video"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 课程资源
class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name="course")
    name = models.CharField(max_length=50, verbose_name="ResourceName")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name="resourceAddress", max_length=100)
    addTime = models.DateTimeField(default=datetime.now, verbose_name="addTime")

    class Meta:
        verbose_name = "CourseResource"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
