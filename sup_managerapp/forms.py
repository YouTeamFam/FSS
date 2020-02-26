#!/usr/bin/python3
# coding: utf-8

from django import forms
from mainapp.models import *
from .models import *
class RoleForm(forms.ModelForm):

    class Meta:
        model = T_Sys_Role
        fields = ['name', 'type']  # '__all__'
        error_messages = {
            'name': {
                'required': '角色名不能为空'
            },
            'type': {
                'required': '角色类型不能为空'
            }
        }
class PtUserForm(forms.ModelForm):

    class Meta:
        model = TUser
        fields = ['u_name', 'u_pwd', 'sex', 'phone']  # '__all__'
        error_messages = {
            'u_name': {
                'required': '用户名不能为空'
            },
            'u_pwd': {
                'required': '密码不能为空'
            },
            'sex': {
                'required': '性别能为空'
            },
            'phone': {
                'required': '电话号码不能为空'
            }
        }

class PtUborkerForm(forms.ModelForm):

    class Meta:
        model = TBroker
        fields = ['b_name', 'b_pwd', 'sex', 'phone','b_uname','company']  # '__all__'
        error_messages = {
            'b_name': {
                'required': '姓名不能为空'
            },
            'b_uname': {
                'required': '用户名不能为空'
            },
            'b_pwd': {
                'required': '密码不能为空'
            },
            'sex': {
                'required': '性别能为空'
            },
            'phone': {
                'required': '电话号码不能为空'
            },
            'company':{
                'required': '公司不能为空'
            }
        }


class FangDongForm(forms.ModelForm):

    class Meta:
        model = TLandlord
        fields = ['l_name','phone','l_uname','l_pwd','sex','sou_num']  # '__all__'
        error_messages = {
            'l_name': {
                'required': '房东名不能为空'
            },
            'phone': {
                'required': '电话不能为空'
            },
            'l_uname': {
                'required': '账号不能为空'
            },
            'l_pwd': {
                'required': '密码不能为空'
            },
            'sex': {
                'required': '性别不能为空'
            },
            'sou_num':{
                'required': '发布房源数不能为空'
            }
        }

class ErShouForm(forms.ModelForm):
    class Meta:
        model = TSecondSource
        fields = ['title', 'ch_state']  # '__all__'
        error_messages = {
            'title': {
                'required': '标题不能为空'
            },
            'ch_state': {
                'required': '审核状态不能为空'
            }
        }

class XinFangForm(forms.ModelForm):
    class Meta:
        model = TSource
        fields = ['title', 'ch_state']  # '__all__'
        error_messages = {
            'title': {
                'required': '标题不能为空'
            },
            'ch_state': {
                'required': '审核状态不能为空'
            }
        }

class MessageForm(forms.ModelForm):

    class Meta:
        model = TMessage
        fields = ['title', 'content']  # '__all__'
        error_messages = {
            'title': {
                'required': '标题不能为空'
            },
            'content':{
                'required': '内容不能为空'
            }
        }



