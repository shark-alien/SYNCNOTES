import os
import sys
import urllib2
import urllib
from datetime import datetime
#from notify import notify
import time
import requests
from urllib import quote_plus as qp



def fetch_srt(song,fileName):

	#print (qp(song.strip()))

	url = 'https://srt-api.herokuapp.com/api?song='+qp(song.strip())
	print url
	lyrics = urllib2.urlopen(url).read()
	
	fw = open(fileName+".srt",'w')

	fw.write(str(lyrics))
	fw.close()





def song_find(path,name):

	artist=""
        song=""
    	extra=""
    	feat=""
	bekar=""

	iname=name
	name= name.replace('.mp3','')
	name= name.replace('.mp4','')
	name= name.replace('.mpg','')
	name= name.replace('.avi','')
	name= name.replace('.mkv','')
	name= name.replace('.flv','')
	name= name.replace('.flac','')
	name= name.replace('.m4a','')

	fileName=name

	for i in range(0,len(name)):
		if name[i] == "[" or name[i] == "(":
    			for x in range(i,len(name)):
        			if name[x] == "]" or name[x]== ")":
            				bekar=name[i:x+1]
            			
	name=name.replace(bekar,"")

	for i in range(0,len(name)):
		try:
    			if (i == name.index("ft")):
				feat=name[i:]
		except:
			feat=""

   	song=name.replace(feat,"")
   	"""
	for i in range(0,len(name)):
        	if name[i]=="-":
            		artist = name[0:i-1]
            		song = name[i+2:]

	

	if ('.mp3' or '.flac' or '.m4a' ) in iname:
		track = eyed3.load(path)
		tag = track.tag
		artist = tag.artist
		song = tag.title	
	"""
	#print song
	#print artist
	#print name
	fetch_srt(song,fileName)
	


def main():
	path = sys.argv[1]
	song = path.split("\\")[-1]
	song_find(path,song)
	#notify()

#start_time = time.time()
#main()
#print("--- %s seconds ---" % (time.time() - start_time))

if __name__ == '__main__':
    main()
