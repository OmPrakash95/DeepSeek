import glob, os
from pprint import pprint
from collections import Counter
import operator 

files = glob.glob('8.mp4*.jpg')

timestamps = [4, 8, 9, 10, 11, 19, 20, 21, 26, 28, 30, 30, 32, 32, 33, 33, 33, 33,33, 33, 33, 34, 34, 34, 34, 35, 35, 35, 35, 35, 35, 36, 36, 36, 36, 36, 36, 36,37, 37, 37, 37, 37, 37, 37, 37, 38, 38, 39, 40, 41, 42, 43, 43, 43, 43, 43, 43,43, 43, 43, 45, 46, 47, 47, 47, 47, 47, 48, 47, 49, 49, 50, 52, 52, 52, 52, 52,52, 53, 53, 54, 57, 58, 60, 65, 69, 72, 73, 75, 76, 80]

#seq_count=Counter(timestamps)

#sorted_seq_count = dict(sorted(seq_count.items(), key=operator.itemgetter(0)))

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

