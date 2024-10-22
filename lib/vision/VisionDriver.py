import io
import os
import sys
from google.cloud import vision

def getLabelsFromFrame(frame_name):
	os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.environ['PROJ_ROOT']+"DeepSearch-01d1b62c37e1.json"	
	vision_client = vision.Client()
	file_name = 'media/'+frame_name

	print "INFO: Processing %s" %(file_name)

	with io.open(file_name, 'rb') as image_file:
    		content = image_file.read()
    		image = vision_client.image(content=content)
		
	labels = image.detect_labels()

	print "INFO: Labels Found"
	return labels