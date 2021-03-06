from django.urls import path
from sup_managerapp.views import *
app_name = "sup_managerapp"
urlpatterns = [
    path("sys_role_manage/",role),
    path("pt_user_manage/",pt_user),
    path("broker_manage/",broker),
    path("fd_manage/", fangdong),
    path('ershou_manage/', ershou),
    path('xinfang_manage/', xinfang),
    path("tui_pt_user/",tuiuser),
    path("tui_mes_fd/",tuifd),
    path("tui_mes_jjr/",tuijjr),
    path("select_tui_user/",selectuser),
    path("select_tui_fd/",selectfd),
    path("select_tui_jjr/",selectjjr),
    path("fasong_user/",fasong_user),
    path("fasong_fd/",fasong_fd),
    path("fasong_jjr/",fasong_jjr),

    path("home_wheel/", home_wheel),
    path('wheel_detail/', WheelView.as_view()),
    path("home_sec/", home_sec),
    path("sec_detail/", SecView.as_view()),
    path("home_rental/", home_rental),
    path('rental_detail/', RentalView.as_view()),
    path("home_xq/", home_xq),
    path('xq_detail/', XqView.as_view()),

    path('edit_role/',EditRoleView.as_view()),
    path('edit_pt_user/',Edit_ptuser_View.as_view()),
    path('edit_broker_user/',Edit_broker_View.as_view()),
    path('xinfang_role/', XinFangView.as_view()),
    path('ershou_role/', ErShouView.as_view()),
    path('fangdong_role/',FangDongView.as_view()),
    path('edit_tui_user/',EditMessageUserView.as_view()),
    path('edit_tui_fd/',EditMessageFdView.as_view()),
    path('edit_tui_jjr/',EditMessageJjrView.as_view()),
]