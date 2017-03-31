import sys
from lib.VideoProcess import getLength, takeScreenshot
from lib.FFMpegLogProcessor import processLog
from pprint import pprint

def main():
    filename = str(sys.argv[1]) 
    print "Filename: %s" %(filename)   
    length = getLength(filename)
    every = 10 #(int(length)*5)/60
    no_ss = int(length)/every
    takeScreenshot(filename,every,no_ss)
    print "Length of the video is %d " % (length)
    timestamp_list=processLog()
    pprint(timestamp_list)    

if __name__== "__main__":
  main()
