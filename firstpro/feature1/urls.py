from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('reg',views.user_reg,name='register'),
    path('login',views.user_login,name="login"),
]