from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi,GetUsers


urlpatterns = [
      path('api/', GetUsers.as_view(), name='users'),
      path('api/register', RegisterApi.as_view()),

]