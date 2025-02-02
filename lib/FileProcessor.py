import glob, os
from pprint import pprint
from collections import Counter
import operator 
import re

def sorted_nicely( l ):
    """ Sorts the given iterable in the way that is expected.
 
    Required arguments:
    l -- The iterable to be sorted.
 
    """
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key = alphanum_key)

def FileRename(media_dir,video_id,timestamps):
	print "INFO: Reading Directory %s for %s.mp4 files" % (media_dir,video_id)
	files = glob.glob(media_dir+video_id+'.mp4*.jpg')
        files = sorted_nicely(files)
	counter=1
	for oldname, ts in zip(files,timestamps):
		splitted_name = oldname.split(".mp4")
		newname=splitted_name[0]+'_'+str(ts)+'_'+str(counter)+'.jpg'
		print "%d : Changing %s to %s \n" %(counter,oldname,newname)
		counter = counter+1
		os.rename(oldname,newname)

	newfiles = glob.glob(media_dir+video_id+'_*.jpg')
	newfiles_count = len(newfiles)
	return newfiles, newfiles_count


