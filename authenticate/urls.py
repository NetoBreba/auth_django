from django.urls import path
from authenticate import views

urlpatterns = [
    path('', views.authenticateUser, name='authenticateUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
]