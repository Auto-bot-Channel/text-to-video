from gtts import gTTS


text = open('text.txt')
story = ""
for lines in text:
	story += lines

myobj = gTTS(text=story, lang='en', slow=False)  
myobj.save("text.mp3") 