from django.urls import path

from mainapp.views import *

urlpatterns = [
path('login/',login ),
path('',index)

]