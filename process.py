import time
import sys

def main():
    filename = str(sys.argv[1])
    f= open("sample.txt","w+")
    for i in range(10):
	
    	f.write("This is line %s \r\n" % filename )
	time.sleep(3)
    f.close()   

if __name__== "__main__":
  main()
