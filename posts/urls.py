from django.urls import path
from . import views

urlpatterns =[
    path('api/', views.PostsApiView.as_view(), name = 'posts'),
    path('api/create/', views.CreatePostApiView.as_view(), name = 'create_post'),
]