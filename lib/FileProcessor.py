import glob, os
from pprint import pprint
from collections import Counter
import operator 


def FileRename(f_regex,timestamps):
	files = glob.glob('8.mp4*.jpg')

	counter=1
	for oldname, ts in zip(sorted(files),timestamps):
		splitted_name = oldname.split(".mp4")
		newname=splitted_name[0]+'_'+str(ts)+'_'+str(counter)+'.jpg'
		print "%d : Changing %s to %s \n" %(counter,oldname,newname)
		counter = counter+1
		os.rename(oldname,newname)

	newfiles = glob.glob('8_*.jpg')

	pprint(newfiles)

	print "Length %d" %(len(newfiles))

