from django.urls import path
from django.urls.conf import include
from . import views


urlpatterns = [

    path('',views.home.HomeView.as_view(), name="home"),
    path('signup/',views.signup.signup, name="signup"),
    path('login/',views.login.user_login, name="login"),
    path('logout/',views.logout.user_logout, name="logout"),
]