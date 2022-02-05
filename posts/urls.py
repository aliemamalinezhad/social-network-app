from django.urls import path
from . import views

urlpatterns =[
    path('api/', views.PostsApiView.as_view(), name = 'posts'),
    path('api/create/', views.CreatePostApiView.as_view(), name = 'create_post'),
    path('api/update/<int:pk>/', views.UpdatePostApiView.as_view(), name = 'update_post'),
    path('api/delete/<int:pk>/', views.DeletePostApiView.as_view(), name = 'delete_post'),
]