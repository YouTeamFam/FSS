from django import forms

from mainapp.models import *

class AdForm(forms.ModelForm):
    class Meta:
        model = TAd
        fields = ['title','ad_bm','ad_url','img_url']  # '__all__'
        error_messages = {

            'title': {
                'required': '标题不能为空'
            },
            'ad_bm': {
                'required': '广告商不能为空'
            },
            'ad_url': {
                'required': '外部链接不能为空'
            }
        }
