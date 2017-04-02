from django.conf.urls import include,url
from . import views

app_name = 'deepseek'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    #deepseek/video/upload
    url(r'video/upload', views.VideoUpload.as_view(), name='video-upload'),
    #deepseek/video/process/1/
    url(r'video/(?P<pk>[0-9]+)/process/', views.VideoProcess, name='video-process'),
    #deepseek/video/queue
    url(r'video/queue/', views.VideoQueue, name='video-queue'),
    #deepseek/video/1/details/
    url(r'video/(?P<pk>[0-9]+)/details/', views.VideoDetails.as_view(), name='video-details'),
    #deepseek/frame/83/media/18_3_13.jpg/video/18/add/
    url(r'frame/(?P<seconds>[0-9]+)/media/(?P<file_name>[\w.]{0,256})/video/(?P<vid>[0-9]+)/add/', views.FrameAdd, name='frame-add'),
    #deepseek/ann/{ROMANCE}/frame/{frame ID}/insert/
    url(r'ann/(?P<label>[\w ]{0,256})/frame/(?P<frame_id>[0-9]+)/add/', views.AnnAdd, name='Ann-add'),
]