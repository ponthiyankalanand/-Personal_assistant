import pyttsx3
engine = pyttsx3.init()
#engine.setProperty('rate',50)  #120 words per minute
sound = engine.getProperty('voices')
engine.setProperty('voice',sound[22].id) 
def speak(ans):
	engine.say(ans)
	engine.runAndWait()

