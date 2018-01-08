from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from .models import UserProfile, EmailVerifyRecord
from django.db.models import Q
from django.views.generic.base import View
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from django.contrib.auth.hashers import make_password
from apps.utils.email_send import sendRegisterEmail
from django.core.urlresolvers import reverse


# 注册
class RegisterView(View):
    def get(self, request):
        registerForm = RegisterForm()
        return render(request, "register.html", {'registerForm': registerForm})

    def post(self, request):
        registerForm = RegisterForm(request.POST)
        if registerForm.is_valid():
            # 注册用户
            userName = request.POST.get("email", "")
            passWord = request.POST.get("password", "")
            userProfile = UserProfile()
            userProfile.username = userName
            userProfile.password = make_password(passWord)  # 加密密码
            userProfile.email = userName
            userProfile.is_active = False
            userProfile.save()
            sendRegisterEmail(userName)
            # return redirect(reverse("login"))
            return render(request, "login.html", {"msg": "register account successfully! please login!"})
        else:
            return render(request, "register.html", {"registerForm": registerForm})


# 激活用户
class ActiveUserView(View):
    def get(self, request, activeCode):
        allRecords = EmailVerifyRecord.objects.filter(code=activeCode)
        if allRecords:
            for record in allRecords:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, "login.html", {"msg": "active account successfully! please login!"})
        else:
            return render(request, "activeFailed.html")


# 密码找回
class ForgetPwdView(View):
    def get(self, request):
        forgetForm = ForgetForm()
        return render(request, "forgetpwd.html", {"forgetForm": forgetForm})

    def post(self, request):
        forgetForm = ForgetForm(request.POST)
        if forgetForm.is_valid():
            email = request.POST.get("email", "")
            sendRegisterEmail(email, "forget")
            return render(request, "sendSuccess.html", {})
        else:
            return render(request, "forgetpwd.html", {"forgetForm": forgetForm})


# 密码重置
class ResetView(View):
    def get(self, request, activeCode):
        allRecords = EmailVerifyRecord.objects.filter(code=activeCode)
        if allRecords:
            for record in allRecords:
                email = record.email
                return render(request, "password_reset.html", {"email": email})
        else:
            return render(request, "activeFailed.html")


# 密码修改
class ModifyView(View):
    def post(self, request):
        modifyForm = ModifyPwdForm(request.POST)
        if modifyForm.is_valid():
            password1 = request.POST.get("password1", "")
            password2 = request.POST.get("password2", "")
            email = request.POST.get("email", "")
            user = UserProfile.objects.get(email=email)
            user.password = make_password(password1)
            user.save()
            return redirect(reverse("pwdResetSuccess"))
        else:
            return render(request, "password_reset.html", {"modifyForm": modifyForm})


# 用户认证
class CustomBackEnd(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # 使用Q连接多个过滤条件
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


# 登录
class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        loginForm = LoginForm(request.POST)
        if loginForm.is_valid():
            userName = request.POST.get("username", "")
            passWord = request.POST.get("password", "")
            # 用户认证
            user = authenticate(username=userName, password=passWord)
            if user is not None:
                if user.is_active:
                    # 认证成功 登陆
                    login(request, user)
                    return redirect(reverse("index"))
                else:
                    return render(request, "login.html", {"msg": "account is not active"})
            else:
                return render(request, "login.html", {"msg": "please check your username and password"})
        else:
            return render(request, "login.html", {"loginForm": loginForm})  # 传递loginForm对象
