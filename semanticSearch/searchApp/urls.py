from django.urls import path
from . import views

urlpatterns = [
    path('uploadVideo/', views.uploadVideo, name = 'upload'),
    path('trainVideos/', views.trainVideos, name = 'train'),
    path('progress/', views.progress, name = 'progress'),
    path('check_progress/', views.check_progress, name='check_progress'),
]