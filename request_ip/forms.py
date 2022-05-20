from attr import attr
from django import forms
from matplotlib.widgets import Widget
from .models import ipInfo

# https://www.learncodewithmike.com/2020/03/django-modelform.html
# https://peilee-98185.medium.com/%E7%94%A8-django-form-%E5%BE%9E%E5%89%8D%E7%AB%AF%E5%82%B3%E8%B3%87%E6%96%99%E5%AD%98%E9%80%B2%E8%B3%87%E6%96%99%E5%BA%AB-c99723e63056

class ipInfoForm(forms.ModelForm):
    class Meta:
        model = ipInfo
        fields = ('server_ipv4',)    # you can use '__all__' if you need all things
        widgets = {
            'server_ipv4': forms.TextInput(attrs={'class':'form-control'})
        }
        labels = {
            'server_ipv4': '伺服器 IP'
        }
