from django.urls import path
from . import views

app_name = 'account'
urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/<int:user_id>/', views.dashboard, name='dashboard'),

]
