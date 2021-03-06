"""DjangoLearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyView
from organization.views import OrgListView
from django.views.static import serve
from DjangoLearning.settings import MEDIA_ROOT

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    # 使用template.as_view 就不需要自己写view.py 适合没有逻辑使用的html
    url('^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url('^login/$', LoginView.as_view(), name="login"),
    url('^register/$', RegisterView.as_view(), name="register"),
    # 添加验证码
    url('^captcha/', include('captcha.urls')),
    # 提取邮箱激活码
    url('^active/(?P<activeCode>.*)/$', ActiveUserView.as_view(), name='active'),
    # 忘记密码
    url('^forget/$', ForgetPwdView.as_view(), name='forget'),
    # 重置密码
    url('^reset/(?P<activeCode>.*)/$', ResetView.as_view(), name='reset'),
    url('^modify/$', ModifyView.as_view(), name='modify_pwd'),
    url('^pwdResetSuccess/$', TemplateView.as_view(template_name="pwdResetSuccess.html"), name='pwdResetSuccess'),

    # 创建organization自己的urls
    url('^org/', include('organization.urls', namespace="org")),
    # 配置静态文件的路径（图片，gif）
    url('^media/(?P<path>.*)/$', serve, {"document_root": MEDIA_ROOT}),

]
