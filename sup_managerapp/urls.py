from django.urls import path
from sup_managerapp.views import *
app_name = "sup_managerapp"
urlpatterns = [
    path("sys_role_manage/",role),
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
    path('edit_role/',EditRoleView.as_view()),
]