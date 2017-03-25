from django.conf.urls import include,url
from . import views

app_name = 'deepseek'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    #deepseek/video/upload
    url(r'video/upload', views.VideoUpload.as_view(), name='video-upload'),
    #deepseek/video/process/1/
    url(r'video/(?P<pk>[0-9]+)/process/', views.VideoProcess, name='video-process'),
]