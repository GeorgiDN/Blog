from django.urls import path
from WebApp.blog.views import PostListView, PostDetailView
from WebApp.blog import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('about/', views.about, name='blog-about'),
]
