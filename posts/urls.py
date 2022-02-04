from django.urls import path
from . import views

urlpatterns =[
    path('api/', views.PostsApiView.as_view(), name = 'posts'),
]