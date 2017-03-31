import sys
from lib.VideoProcessor import getLength, takeScreenshot
from lib.FFMpegLogProcessor import processLog
from lib.FileProcessor import FileRename
from pprint import pprint

def main():
    filename = str(sys.argv[1])
    video_name = filename[6:]
    video_id = video_name[:4]
    print "Filename: %s" %(filename)   
    video_length = getLength(filename)
    takeScreenshot(filename)
    print "Length of the video is %d " % (length)
    timestamp_list=processLog()
    FileRename(

if __name__== "__main__":
  main()
