from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # Главная страница
    path('', views.index, name='index'),  # blog:index
    # Детали поста
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),  # blog:post_detail
    # Посты категории
    path('category/<slug:category_slug>/',
         views.category_posts, name='category_posts'),  # blog:category_posts
]
