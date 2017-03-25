from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Video, Frame, Annotation
#from .forms import UserForm
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
	a = subprocess.Popen(['python', 'manage.py', 'some_command'])
	return render(request, 'deepseek/process.html',{ 'video_id' : pk})