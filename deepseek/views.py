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


def VideoProcess(request, pk):
	video = Video.objects.get(id=pk)
	path = video.video_path
	a = subprocess.Popen(['python', 'VideoProcess.py', 'media'+path.name[1:] ])
	video.process_id=a.pid
	video.save()
	return redirect('deepseek:video-queue') 
	#return render(request, 'deepseek/queue.html')
	#return render(request, 'deepseek/queue.html',{ 'video_id' : pk, 'process_id' : a.pid })

def VideoQueue(request):
	queue = Video.objects.filter(process_id__gt = 0)
	return render(request, 'deepseek/queue.html', { 'queue_list': queue })