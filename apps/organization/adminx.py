import xadmin
from .models import *


class CityDictAdmin(object):
    # 显示
    list_display = ['name', 'desc', 'addTime']
    # 搜索
    search_fields = ['name', 'desc']
    # 筛选
    list_filter = list_display


class CourseOrgAdmin(object):
    # 显示
    list_display = ['name', 'desc', 'category', 'clickNum', 'address', 'favoriteNum', 'studentNum', 'courseNum', 'city',
                    'addTime']
    # 搜索
    search_fields = ['name', 'desc', 'category', 'clickNum', 'address', 'favoriteNum', 'studentNum', 'courseNum',
                     'city']
    # 筛选
    list_filter = list_display


class TeacherAdmin(object):
    # 显示
    list_display = ['name', 'workYears', 'workCompany', 'level', 'features', 'favoriteNum', 'organization', 'addTime']
    # 搜索
    search_fields = ['name', 'workYears', 'workCompany', 'level', 'features', 'favoriteNum', 'organization']
    # 筛选
    list_filter = list_display


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
