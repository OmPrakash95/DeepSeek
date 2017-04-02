from __future__ import unicode_literals
from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.


class Video(models.Model):
	name = models.CharField(max_length=250)
	description = models.CharField(max_length=500)
	video_path = models.FileField(upload_to='temp')
	process_id = models.IntegerField(default=0)
	is_finish_process = models.BooleanField(default=False)

	def save(self, *args, **kwargs):
		super(Video, self).save(*args, **kwargs)
		video_path=self.video_path
		if video_path:
			oldfile = self.video_path.name
			newfile= str(self.pk)+'.mp4'

			if newfile !=oldfile:
				self.video_path.storage.delete(newfile)
				self.video_path.storage.save(newfile,video_path)
				self.video_path.name=newfile
				self.video_path.close()
				self.video_path.storage.delete(oldfile)

		super(Video, self).save(*args, **kwargs)

	#def get_absolute_url(self):
	#	return reverse('videos:detail', kwargs={'pk' : self.pk})

	def __str__(self):
		return self.name+' - '+self.description

	def get_absolute_url(self):
		return reverse('deepseek:video-process', kwargs={'pk' : self.pk})

class Frame(models.Model):
	video_id = models.ForeignKey(Video, on_delete=models.CASCADE)
	at_duration = models.IntegerField()
	frame_path = models.CharField(default='',max_length=100)

	def __str__(self):
		return str(self.video_id)+' - '+ str(self.at_duration)

class Annotation(models.Model):
	annotation_name = models.CharField(max_length=100)
	frames = models.CharField(max_length=1000)

	def __str__(self):
		return self.annotation_name+' - '+ self.frames