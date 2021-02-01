from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.all_post, name='all_post'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('add-post/<int:user_id>/', views.add_post, name='add_post'),
    path('post-delete/<int:user_id>/<int:post_id>/', views.delete_post, name='post_delete'),
]
