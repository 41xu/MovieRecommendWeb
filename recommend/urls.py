from django.urls import path
from . import views


urlpatterns = [
    # path('login/',views.login),
    # path('register/',views.reg),
    path('search-form/',views.search_form),
    path('search/',views.search)
]
