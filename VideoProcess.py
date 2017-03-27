import time
import sys
import subprocess
import shlex
import re

def main():
    filename = str(sys.argv[1])
    log_file_name = filename+'.txt'
    
    length = getLength(filename)
    every = 10 #(int(length)*5)/60
    no_ss = int(length)/every
    takeScreenshot(filename,every,no_ss)
    print "Length of the video is %d - take screenshot every %d seconds and No. of screenshot is %d " % (length, every, no_ss)

def takeScreenshot(filename, every, no_ss):
	command = 'ffmpeg -ss 3 -i '+str(filename)+' -vf "select=gt(scene\,0.3)" -vf fps=fps=1/'+str(every)+' -frames:v '+str(no_ss)+' -vsync vfr '+str(filename)+'%02d.jpg'
	subprocess.call(shlex.split(command))

def getLength(filename):
	process = subprocess.Popen(['ffmpeg',  '-i', filename], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	stdout, stderr = process.communicate()
	matches = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),", stdout, re.DOTALL).groupdict()
	total = 0.0;
	total += float(matches['hours'])*60
	total += float(matches['minutes'])*60
	total += float(matches['seconds'])
	return total

if __name__== "__main__":
  main()
