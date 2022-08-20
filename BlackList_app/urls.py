from django.urls import path, include

from . import views

app_name= 'BlackList_app'
urlpatterns = [
    #Include default auth urls
    path('', views.homepage,name="homepage"),
    path('login', views.login,name="login"),
    path('signup', views.signup,name="signup"),
    path('menu_student',views.menu_student,name="menu_student"),
    path('menu_institution',views.menu_institution,name="menu_institution"),
    path('complaint',views.complaint,name='complaint'),
    path('notifications',views.notifications,name='notifications'),
    path('profile',views.profile,name='profile'),
    path('messege',views.messege,name='messege'),
    
]