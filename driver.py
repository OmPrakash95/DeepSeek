import sys
import os
from lib.VideoProcessor import getLength, takeScreenshot
from lib.FFMpegLogProcessor import processLog
from lib.FileProcessor import FileRename
from lib.FrameProcessor import ProcessFrames
from pprint import pprint

def main():
    filename = str(sys.argv[1])
    media_dir = 'media/'
    video_name = filename[6:]
    video_id = video_name[:-4]
    print "INFO: Filename: %s" %(filename)   
    video_length = getLength(filename)
    takeScreenshot(filename)
    print "INFO: Length of the video is %d " % (video_length)
    timestamp_list=processLog()
    print "INFO: Media Dir: %s Video ID: %s Timestamp_list: " %(media_dir,video_id)
    #pprint(timestamp_list)
    newfiles_list,newfiles_count = FileRename(media_dir,video_id,timestamp_list)
    print "INFO: Count of Files after renaming: %d" %(newfiles_count)
    ProcessFrames(newfiles_list,video_id)
    #pprint(newname_list)

if __name__== "__main__":
  os.environ["PROJ_ROOT"] = "/home/prakash/neural/"
  main()
  
