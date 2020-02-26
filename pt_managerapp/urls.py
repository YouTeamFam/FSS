#!/usr/bin/python3
#_*_coding:utf-8_*_
from django.urls import path
from pt_managerapp.views import *


urlpatterns = [
    #审核广告
    path('ad_check/',AdMessageView.as_view()),
    path('message_audit/',AdAuditMessage.as_view()),
    path('ad_list/',ad_message),
    path('ad_check_record/',ad_check_record),
    path('ad_list_all/',ad_all),

    #审核房源
    path('house_check/',x_fang_source),
    path('house_check_j/',j_fang_source),
    path('x_check/',xf_check),
    path('j_check/',jf_check),
    path('x_message/',x_check_message),
    path('j_message/',j_check_message),
    path('x_one/',xf_check_record),
    path('j_one/',jf_check_record),
    path('fy_check_list/',fy_check_list),

    #发帖
    path('ft_check/',post_message),
    path('ft_details/',check_ft_details),

    #举报投诉
    path('complaint/',complaint_view),
    path('dispose_complaint/',dispose_complaint_view),
    path('select_all_complaint/',select_all_complaint),
    path('detail_content/',detail_content_view)
]