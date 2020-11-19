from django.urls import path
from . import views


urlpatterns = [
    path('', views.article_list_create), # get post
    path('<int:article_pk>/', views.article_update_delete_detail), # put delete get
    path('<int:article_pk>/comment/', views.comment_create), # post
    path('<int:article_pk>/comment/<int:comment_pk>/', views.comment_update_delete), # put delete
    path('<int:article_pk>/like/', views.like_create), # post
]