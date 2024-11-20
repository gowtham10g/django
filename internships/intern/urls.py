from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path('', views.home, name="home"),
    path("courses.html", views.courses_view, name="courses"),    
]
