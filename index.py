#import files
import os
import socket
import pyttsx3
import threading 
from time import *
from trashh import *
from musicplayer import *
from speech import *
from speechrec import *
from speechex import *
from questionNueron import *
#internet checking
def internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except Exception as ex:
        
        return False
#text to speech
engine = pyttsx3.init()
#engine.setProperty('rate',50)  #120 words per minute
sound = engine.getProperty('voices')
engine.setProperty('voice',sound[22].id) 
def speak(ans):
	engine.say(ans)
	engine.runAndWait()
#switch
def switch_query(squery):
   if squery == "play music":
      print("hi")
      musicstart()
   elif (squery == "sorry"):
      print('sorry')
   elif (squery == "stop music"):
      print('stoping music ') 
      musicStop() 
      
   else:
      findAnswer(squery)
      print("searchig in file")
      answer = speechExtraction(squery)
      speak(answer)
#main
def main1():
   while(True):
     print(threading.enumerate())
     sans = speechtotext()
     var = sans.lower() 
     var2 = internet()
     print(var,var2)
     if (var=='hello tara' and var2==True):
       speak('hello, How can i Help u?')
       dummyQuery=speechtotext()
       query = dummyQuery.lower()
       print(query)
       print(switch_query(query)) 
     elif (var2==False):
       speak('check your internet connection')
     else:
       print("waiting for your call")
ob1 = threading.Thread(target=main1,name='thread1')
ob1.start()






