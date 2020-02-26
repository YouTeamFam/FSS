from django.urls import path

from ad_managerapp.views import *
app_name = "ad_managerapp"
urlpatterns = [
    path('ad_manage/',ad),
    # path("pt_user_manage/",),
    # path("broker_manage/",),
    # path("s_house_manage/",),
    # path("n_house_manage/",),
    # path("tui_pt_user/",),
    # path("tui_ad/",),
    # path("home_wheel/",),
    # path("home_s_house/",),
    # path("home_select_house/",),
    # path("home_select_xq/",),
    path('ad_role/',AdView.as_view()),
]