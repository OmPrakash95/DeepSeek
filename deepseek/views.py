from django.db.models.functions import Concat, Value
from django.views.decorators.csrf import csrf_exempt
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Video, Frame, Annotation
#from .forms import UserForm
import os
import signal
import subprocess


class IndexView(generic.ListView):
	template_name = 'deepseek/index.html'
	context_object_name = 'all_videos'


	def get_queryset(self):
		return Video.objects.all()

class VideoUpload(CreateView):
	model = Video
	fields = ['name', 'description', 'video_path']

class VideoDetails(generic.DetailView):
	model = Video
	template_name = 'deepseek/detail.html'


def VideoProcess(request, pk):
	video = Video.objects.get(id=pk)
	path = video.video_path
	a = subprocess.Popen(['python', 'driver.py', 'media/'+str(video.id)+'.mp4' ])
	video.process_id=a.pid
	video.save()
	return redirect('deepseek:video-queue') 
	#return render(request, 'deepseek/queue.html')
	#return render(request, 'deepseek/queue.html',{ 'video_id' : pk, 'process_id' : a.pid })

def VideoQueue(request):
	queue = Video.objects.filter(process_id__gt = 0)
	return render(request, 'deepseek/queue.html', { 'queue_list': queue })

@csrf_exempt
def FrameAdd(request,seconds,file_name,vid):
	#url(r'frame/(?P<seconds>[0-9]+)/media/(?P<file_name>[\w.]{0,256})/video/(?P<video_id>[0-9]+)/add/', views.FrameAdd, name='frame-add'),
	video = Video.objects.get(id=vid) # assuming pers_type is unique
	frame = Frame.objects.create(video_id=video, at_duration=seconds, frame_path='media/'+file_name)
	
	return render(request, 'deepseek/frameadd.html', {'frame': frame.id})

@csrf_exempt
def AnnAdd(request, label, frame_id):
	annotation = Annotation.objects.filter(annotation_name__contains = label ).first()
	response = ''
	if not annotation:
		#Add New Annotation
		Annotation.objects.create(annotation_name=label.lower(), frames=str(frame_id)+',')
		response = "No Label Called "+label+"<br><h1>Added New!</h1>"
	else:
		#Update existing Annotation
		Annotation.objects.filter(pk=annotation.id).update(frames=Concat('frames',Value(str(frame_id)+',')))
		response = "There is a Label called "+label+"<br>Appending new Label"
	#Annotation.objects.create(annotation_name=label.lower(), frames=str(frame_id)+',')
	return render(request, 'deepseek/annadd.html', { 'response': response })
