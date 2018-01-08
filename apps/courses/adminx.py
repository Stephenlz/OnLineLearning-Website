import xadmin
from .models import *


class CourseAdmin(object):
    # 显示
    list_display = ['name', 'desc', 'detail', 'degree', 'learnTime', 'studentNum', 'favoriteNum', 'clickNum', 'addTime']
    # 搜索
    search_fields = ['name', 'desc', 'detail', 'degree']
    # 筛选
    list_filter = list_display


class LessonAdmin(object):
    # 显示
    list_display = ['course', 'name', 'addTime']
    # 搜索
    search_fields = ['course', 'name']
    # 筛选
    list_filter = list_display


class VideoAdmin(object):
    # 显示
    list_display = ['lesson', 'name', 'addTime']
    # 搜索
    search_fields = ['lesson', 'name']
    # 筛选
    list_filter = list_display


class CourseResourceAdmin(object):
    # 显示
    list_display = ['course', 'name', 'download', 'addTime']
    # 搜索
    search_fields = ['course', 'name']
    # 筛选
    list_filter = list_display


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
