from django.urls import path
from . import views

app_name = 'music_app'

urlpatterns = [
    path("user/<int:pk>/", views.user_detail, name="user_detail"),
    path("user", views.user_list, name="user_detail"),

    path("songs", views.user_list, name="Songs_detail"),
    path("songs/<int:pk>/", views.user_detail, name="Songs_detail"),
]
