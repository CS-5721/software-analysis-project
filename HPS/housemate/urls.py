from django.urls import path

from . import views

app_name="housemate"
urlpatterns = [
    path('', views.index, name='index'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('user_login', views.user_login, name='user_login'),
    path('myboard', views.myboard, name='myboard'),
    path('register', views.register, name='register'),
    path('registerLandlord', views.registerLandlord, name='registerLandlord'),
    path('profile_view', views.profile_view, name='profile_view'),
    path('edit', views.edit, name='edit')
]