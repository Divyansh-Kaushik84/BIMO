import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
'''
Importing required packages,libraries,modules for the program
'''


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
'''
Here the voices are selected for the assistant
[0] is for Male
[1] is for Female
'''

def speak(audio):

    '''
    This function is created to allow the program to speak
    '''
    engine.say(audio)
    engine.runAndWait()

def wishMe():

    '''
    Created for the program to recognize the time of the day and wish accordingly
    '''

    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning Sir!!!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!!!")

    else:
        speak("Good Evening Sir!!!")
         
    speak("I am Bmo How may I help You")

def takeCommmand():
    '''Takes microphone input from the user and will return String as output'''

    r=sr.Recognizer()   #Recognizer class is used to recognize the input audio
 
    with sr.Microphone() as source:

        print("Listening...") # Reminds that the program is listening 

        r.pause_threshold=1  # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold=10
        '''We can also increase the energy required to record so that we can capture only the clear noises
        '''

        audio=r.listen(source) #stores the audio inputted

    try:#incase any eroor occur

        print("Recognizing...")

        query=r.recognize_google(audio,language='en-in')#choosing search engine to recognize the audio and storing the value after recognizing the audio
        
        print(f"You Said: {query}\n")#f string is used to place the value of variable inside the string
    
    except Exception as e:#if exception occurs

        # print(e) 
        print("Sorry Sir, I didnt catch that. Say that again please...")
        return "None"#a string none is returned
    return query

if __name__=="__main__":
    wishMe()
    takeCommmand()