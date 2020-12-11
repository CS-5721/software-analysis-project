from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin_login', views.admin_log, name='admin_log'),
    path('user_login', views.user_log, name='user_log'),
    path('myboard', views.myboard, name='myboard'),
    path('register', views.register, name='register'),
    path('registerLandlord', views.registerLandlord, name='registerLandlord'),
    path('profile_view', views.profile_view, name='profile_view'),
]