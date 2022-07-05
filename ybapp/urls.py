from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),    
    path('login', views.login_user, name='login'),
    path('register', views.register, name='register'),
    path('user_detail', views.user_detail,name='user_detail'),
    path('adduserdetail', views.adduserdetail,name='adduserdetail'),
    path('logout', views.logoutuser,name='logout'),
]  