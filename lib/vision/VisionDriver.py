import io
import os
import sys
from google.cloud import vision

def getLabelsFromFrame(frame_name):
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "file=/home/prakash/neural/DeepSearch-01d1b62c37e1.json"	
	vision_client = vision.Client()
	file_name = 'media/'+frame_name

	print "INFO: Processing %s" %(file_name)

	with io.open(file_name, 'rb') as image_file:
    		content = image_file.read()
    		image = vision_client.image(content=content)
		
	labels = image.detect_labels()
	if len(labels)>0:
		print "INFO: Labels NOT found"
	else:
		print "INFO: Labels Found"
		return labels