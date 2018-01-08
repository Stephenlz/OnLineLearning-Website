import xadmin
from .models import *


class UserAskAdmin(object):
    # 显示
    list_display = ['name', 'mobile', 'courseName', 'addTime']
    # 搜索
    search_fields = ['name', 'mobile', 'courseName']
    # 筛选
    list_filter = list_display


class CourseCommentsAdmin(object):
    # 显示
    list_display = ['user', 'course', 'comments', 'addTime']
    # 搜索
    search_fields = ['user', 'course', 'comments']
    # 筛选
    list_filter = list_display


class UserFavoriteAdmin(object):
    # 显示
    list_display = ['user', 'dataId', 'dataType', 'addTime']
    # 搜索
    search_fields = ['user', 'dataId', 'dataType']
    # 筛选
    list_filter = list_display


class UserMessageAdmin(object):
    # 显示
    list_display = ['user', 'message', 'hasRead', 'addTime']
    # 搜索
    search_fields = ['user', 'message', 'hasRead']
    # 筛选
    list_filter = list_display


class UserCourseAdmin(object):
    # 显示
    list_display = ['user', 'course', 'addTime']
    # 搜索
    search_fields = ['user', 'course']
    # 筛选
    list_filter = list_display


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
