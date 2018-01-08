import xadmin
from .models import EmailVerifyRecord, PageBanner
from xadmin import views


# 主题配置
class BaseSettings(object):
    enable_themes = True
    use_bootswatch = True


# 全局配置
class GlobalSettings(object):
    site_title = "Management System"
    site_footer = "StephenArwen"
    menu_style = "accordion"


class EmailVerifyRecordAdmin(object):
    # 显示
    list_display = ['code', 'email', 'sendType', 'sendTime']
    # 搜索
    search_fields = ['code', 'email', 'sendType']
    # 筛选
    list_filter = ['code', 'email', 'sendType', 'sendTime']


class PageBannerAdmin(object):
    # 显示
    list_display = ['title', 'image', 'url', 'index', 'addTime']
    # 搜索
    search_fields = ['title', 'image', 'url', 'index']
    # 筛选
    list_filter = ['title', 'image', 'url', 'index', 'addTime']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(PageBanner, PageBannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
