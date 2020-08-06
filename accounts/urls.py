from django.urls import path
from . import views
urlpatterns = [
    path('signUp', views.signUp, name="signUp"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name='logout')

]