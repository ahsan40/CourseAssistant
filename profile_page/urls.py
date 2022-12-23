from django.urls import path

from . import views

urlpatterns = [
    path('profile_2', views.add_content, name="add_content"),
    path('profile',views.Index_2, name='Index_2'),
    path('', views.comment_section, name="comment_section")
]