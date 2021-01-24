from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.all_post, name='all_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
]
