import re
from pprint import pprint

def getSecFromTime(time_string):
    time_index = time_string.split(':')
    hours = int(time_index[0])
    mins = int(time_index[1])
    secs = float(time_index[2])
    total = int(hours*60+mins*60+secs)
    return total

def processLog():
    print "INFO: Started processing FFMPEG Log"
    f = open('media/ffreport.log','r')
    outf = open('media/ffparsed.log','w')
    element = ''
    elements = []
    timestamp= []
    keywords = ['select_out:0']
    i=0
    pattern = re.compile('|'.join(keywords))
    for line in f:
        if pattern.search(line):
            nl=line.split()
            element = nl[5]
            if '=' in element and ':' in element:
                time_index = element.split('=')
                #print "%s" %(time_index[1])
                seconds = getSecFromTime(time_index[1])
                timestamp.append(seconds) 
            elif ':' in element:
                outf.write(str(i)+element+"\n")
                time_index = element.split(':')
                seconds=int(float(time_index[1]))
                timestamp.append(seconds)
    #pprint(time)
    print "INFO: Completed processing FFMPEG Log"
    print "No. of Frames: %d" %(len(timestamp))
    return timestamp


if __name__== "__main__":
  processLog()
