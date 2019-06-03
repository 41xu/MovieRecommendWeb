from django.urls import path, re_path
from . import views


urlpatterns = [
    path('',views.default),
    re_path(r"(\w+)/$",views.userInfo)

]
