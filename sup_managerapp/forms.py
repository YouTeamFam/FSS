#!/usr/bin/python3
# coding: utf-8

from django import forms
from .models import T_Sys_Role


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

# class SysUserForm(forms.ModelForm):
#
#     class Meta:
#         model = TSysUser
#         fields = ['username', 'auth_string', 'role_id', 'nick_name']  # '__all__'
#         error_messages = {
#             'username': {
#                 'required': '账号不能为空'
#             },
#             'auth_string': {
#                 'required': '口令不能为空'
#             },
#             'role_id': {
#                 'required': '系统用户角色不能为空'
#             }
#         }