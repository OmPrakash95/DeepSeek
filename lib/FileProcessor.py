import glob, os
from pprint import pprint
from collections import Counter
import operator 


def FileRename(media_dir,video_id,timestamps):
	print "INFO: Reading Directory %s for %s.mp4 files" % (media_dir,video_id)
	files = glob.glob(media_dir+video_id+'.mp4*.jpg')

	counter=1
	for oldname, ts in zip(sorted(files),timestamps):
		splitted_name = oldname.split(".mp4")
		newname=splitted_name[0]+'_'+str(ts)+'_'+str(counter)+'.jpg'
		print "%d : Changing %s to %s \n" %(counter,oldname,newname)
		counter = counter+1
		os.rename(oldname,newname)

	newfiles = glob.glob(media_dir+video_id+'_*.jpg')
	newfiles_count = len(newfiles)
	return newfiles, newfiles_count


