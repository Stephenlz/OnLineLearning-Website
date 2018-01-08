from django import forms
from captcha.fields import CaptchaField
from .models import UserProfile


# form.py 用于对提交的表单进行初始的检测
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserProfile.objects.filter(email=email):
            raise forms.ValidationError("Email address already used!")
        return email


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not UserProfile.objects.filter(email=email):
            raise forms.ValidationError("Email address doesn't exist!")
        return email


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=5)
    password2 = forms.CharField(required=True, min_length=5)

    def clean(self):
        cleaned_data = super(ModifyPwdForm, self).clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords don't match!")
        return cleaned_data
