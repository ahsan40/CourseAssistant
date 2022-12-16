from django.urls import path
from . import views

urlpatterns = [
    path('re', views.request_content, name="request_content"),
    path('', views.home, name="home"),
    path('messages', views.messages, name="messages"),
    path('chat', views.chat, name="chat"),
]
