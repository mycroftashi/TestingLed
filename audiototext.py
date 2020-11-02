import speech_recognition as sr # create the recognizer
r = sr.Recognizer() # define the microphone
with sr.AudioFile('I-dont-know.wav') as source:
   audio_text = r.listen(source)
   try:
       text = r.recognize_google(audio_text)
       print('Converting audio transcripts into text ...')
       print(text)
   except:
       print('Sorry.. run again...')