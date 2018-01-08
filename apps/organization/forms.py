from django import forms
from operation.models import UserAsk
import re

# 调用ModelForm
# 用户咨询表单
class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'courseName']

    # 对mobile进行检查
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = '\d{10}'
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("Mobile Number Error")
