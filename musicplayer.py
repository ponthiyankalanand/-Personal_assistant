from __future__ import unicode_literals
import youtube_dl
import urllib.request
import urllib.parse
import re
import os
import time
from threading import *
from trashh import *
from speech import *
from speechrec import *
from youtube_dl import YoutubeDL
import playsound
#from pygame import mixer # Load the required library
import glob
def musicFinder():
	speak("which song you want to play?")
	var = speechtotext()
	print (var)
	temp1 = var.split()
	fileName = []
	for name in sorted(glob.glob('/media/anand/Media/tara/music/*')):
		temp2 = name.split()
		tempCount = 0
		for serch in temp2:
			if serch in temp1:
				tempCount = tempCount + 1
				val=name 
                #print(val)
				fileName.append(val)

	List = fileName
    #print (List)
	counter = 0
	c="fail"
	file = "fail"     
	for i in List: 
		curr_frequency = List.count(i) 
		if(curr_frequency> counter): 
			counter = curr_frequency 
			file = i
			c="true"
	if(c == "true" ):
		playsound.playsound(file)

	elif (file == "fail"):
		speak("i can't find that sond in your playlist.")
		speak("But i can download that music for. yes or no ?")
		temp3 = speechtotext()
		if (temp3 == "yes"):
            #file = runmusic()
			print("inside music player")
			speak('please repeate the music name') 
			songquery=speechtotext()
			speak('Download started please wait') 
			query_string = urllib.parse.urlencode({"search_query" :songquery})
			html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
			search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
			link="http://www.youtube.com/watch?v=" + search_results[0]
			print(link)
			ydl_opts = {
				'format': 'bestaudio/best',
				'outtmpl': '/media/anand/Media/tara/music/%(title)s.%(ext)s',
				'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192',
					}],
				}
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
				ydl.download(["http://www.youtube.com/watch?v=" + search_results[0]])
				info_dict = ydl.extract_info(link, download=True)
				fn = ydl.prepare_filename(info_dict)
				fn = fn[:-4]
				extn="mp3"
				fn=fn+extn
				print(fn) 
				file = fn
			playsound.playsound(file,True)
		else:
			print("exiting")
	else :
		print("exiting")
#player
#def infun(filef):
 #   print(filef)
  #  playsound.playsound(filef, True)
#deleting the downloaded file
t = Thread(target=musicFinder,name='thread2')
def musicstart():
	t.start()
def musicStop():
	t.join(0)

 


 


