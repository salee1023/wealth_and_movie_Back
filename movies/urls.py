from django.urls import path
from . import views


urlpatterns = [
    path('', views.movie_list_create),
    path('<int:movie_pk>/', views.movie_update_delete_detail),
]