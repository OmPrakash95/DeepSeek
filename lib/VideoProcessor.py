import time
import sys
import subprocess
import shlex
import re
import os

def takeScreenshot(filename):
#	command = 'ffmpeg -ss 3 -i '+str(filename)+' -vf "select=gt(scene\,0.3)" -vf fps=fps=1/'+str(every)+' -frames:v '+str(no_ss)+' -vsync vfr '+str(filename)+'%02d.jpg'
	print "INFO: GETTING SCREENSHOT FROM FILE %s" % (filename)
	os.environ["FFREPORT"] = "file=/home/prakash/neural/media/ffreport.log"	
	command = 'ffmpeg -i '+str(filename)+' -vf "select=eq(pict_type\,I)" -vf "select=gt(scene\,0.3)*lt(scene\,0.7)" -vsync vfr -q:v 1 '+str(filename)+'%d.jpg'
	subprocess.call(shlex.split(command))

def getLength(filename):
	print "INFO: GETTING LENGTH OF FILE %s" % (filename)
	process = subprocess.Popen(['ffmpeg',  '-i', filename ], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
	total = 0.0;
	total += float(matches['hours'])*60
	total += float(matches['minutes'])*60
	total += float(matches['seconds'])
	return total

