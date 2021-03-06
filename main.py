import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import time
import wikipedia
import pyjokes
import webbrowser
import os
from playsound import playsound
import wolframalpha
import requests
import json



listener = sr.Recognizer()
engine = pyttsx3.init()
engine. setProperty("rate", 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rounds = 0
listening = True




def talk(text):
    engine.say(text)
    engine.runAndWait()
    
    
    
def wishMe():
    hour = datetime.datetime.now().hour
    
    if hour>0 and hour<12:
        print('Rise and shine Rohaan')
        talk('Top of morning to you rohan.')
        talk('what can i do for you.')
    
    elif hour>12 and hour<18:
        print('goood afterrnoon roohaan')
        talk('goood afternoon rohan. I hope you are having a great day')
        talk('what can i do for you.')
    
    else:
         print('goood eveningggg roohaan')
         talk('I hope you are enjoying your evening buddy.')
         talk('Tell me how can i help you.')
    
      
        

      



 

def take_command():
     global rounds
    
     rounds = rounds + 1
     if rounds == 1:
        wishMe()
        playsound('sound.mp3')
        
     else:        
        playsound('sound2.mp3')



     try:
        print('Hello Rohan')
        my_mic = sr.Microphone()
        with my_mic as source:
            print('I am Listening...')
            voice = listener.listen(source)
            listener.adjust_for_ambient_noise(source)
            command = listener.recognize_google(voice)
            command = command.lower()
           
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)
            
    
     except:
         pass
     return command

    
        


def tell_city():
    talk('what is the name of the city?')
    playsound('sound2.mp3')
    try:
        print('what is the name of the city?')
        my_mic2 = sr.Microphone()
        with my_mic2 as source2:
            print('Listening...')
            voice = listener.listen(source2)
            listener.adjust_for_ambient_noise(source2)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(command) 
           
            
    
    except:
        pass
    
    return command

    

def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
        
    elif 'about' or 'who is' in command:
        if 'about' in command:
            person = command.replace('tell me about', '')
        else:
            person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)

    elif 'date' in command:
        date = datetime.date.today().strftime('%Y, %B %d')
        talk('todays date is' + date)
        
    elif 'are you single' in command:
        talk('I am in relationship with wifi')
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        
    elif 'for me' in command:
        talk('I am Jarvis version 1 point O, your personal assistant.   '
             '\n I can open youtube, google chrome, gmail and stackoverflow for you.   '
             '\n I can also predict date and time '
             '\n click beautifull selfies for your handsome face and'
             '\n I can get top headlines for you from times of India.   '
             '\n You can ask me mathematical and geographical questions too.   '
             '\n I can tell you hot bollywood and hollywood gossips   ' 
             'and \n i can also tell you the weather for you to plan your day . ')
        
        
    elif 'headlines' in command:
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from Times of India, happy reading')
        
        
    elif 'search' in command:
        command = command.replace('search', '')
        print(command + 'good')
        webbrowser.open_new_tab(command)
        
    elif 'youtube' in command:
        webbrowser.open_new_tab("https://www.youtube.com/")
        talk('Youtube is now open, enjoy')
        
    elif 'google' in command:
        webbrowser.open_new_tab("https://www.google.com/")
        talk('Google is now open, enjoy')
        
    elif 'gmail' in command:
        webbrowser.open_new_tab("https://www.gmail.com/")
        talk('gmail is now open, enjoy')

        
    elif 'meaning of' in command:
        command = command.replace('what is the', '')
        command = command.replace('meaning of', '')
        means = wikipedia.summary(command, 1)
        talk(means)
        print(means)
        
    elif 'capital' in command:
        app_id = '5X639U-WAP7U9827U'
        client = wolframalpha.Client(app_id)
        res = client.query(command)
        ans = next(res.results).text
        talk(ans)
        print(ans)
        
        
    elif  "where is" in command:
        command = command.replace("where is", "" )
        location_url = 'https://www.google.co.in/maps/place/' + command
        talk("Hold on Rohan, I will show you where " + command + " is.")
        webbrowser.open_new_tab(location_url)

    elif "calculate" or "+" or "-" or "*" or "/" in command:
        app_id = '5X639U-WAP7U9827U'
        client = wolframalpha.Client(app_id)
        math_res = client.query(command)
        math_ans = next(math_res.results).text
        talk("it is equal to " + math_ans)
        print(math_ans)
        
    
    elif 'weather' or 'weather like' in command:
        global listening
        
        API_URL = "http://api.openweathermap.org/data/2.5/weather?";
                
        API_KEY = "f13e951b419a4489bbb36891974f5443"
        
        
        location = tell_city()
        complete_url =  API_URL + "appid=" + API_KEY + "&q=" + location
        
        js = requests.get(complete_url).json()
        
        if js["cod"] == "404":
            talk("sorry could not find the location you asked for")
        
        else:

            weather = js["main"]
            current_tempratureK = weather["temp"]
            current_humidity = weather["humidity"]
            weather_description = js["weather"][0]["description"]
            current_tempratureC = round(current_tempratureK - 273.15)
            
            talk("temprature in celsius unit is " +
                 str(current_tempratureC) + 
                 "\n humidity in percentage is " + 
                 str(current_humidity) + 
                 "\n currently " + 
                 str(weather_description))
            
            print("temprature in celsius unit is " +
                 str(current_tempratureC) + 
                 "\n humidity in percentage is " + 
                 str(current_humidity) + 
                 "\n currently " + 
                 str(weather_description))
            
            
             
    else:
        talk('pardon me, can you please repeat that again.')
        
#=============================================================

def run_jarvis_chat(chat):
    print(chat)
    if 'play' in chat:
        song = chat.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
        
    elif 'time' in chat:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
        print(time)
     
    elif "who is" in chat:
        person = chat.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    

    elif 'date' in chat:
        date = datetime.date.today().strftime('%Y, %B %d')
        print('todays date is ' + date)
        talk('todays date is' + date)
        
        
    elif 'are you single' in chat:
        talk('I am in relationship with wifi')
        print('I am in relationship with wifi')
        
    elif 'joke' in chat:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
        
    elif 'for me' in chat:
        talk('I am Jarvis version 1 point O, your personal assistant.   '
             '\n I can open youtube, google chrome, gmail and stackoverflow for you.   '
             '\n I can also predict date and time '
             '\n I can get top headlines for you from times of India.   '
             '\n You can ask me mathematical and geographical questions too.   '
             '\n I can tell you hot bollywood and hollywood gossips   ' 
             'and \n i can also tell you the weather for you to plan your day . ')
        
        print('I am Jarvis version 1.O, your personal assistant.   '
             '\n I can open youtube, google chrome, gmail and stackoverflow for you.   '
             '\n I can also predict date and time '
             '\n I can get top headlines for you from times of India.   '
             '\n You can ask me mathematical and geographical questions too.   '
             '\n I can tell you hot bollywood and hollywood gossips   ' 
             'and \n i can also tell you the weather for you to plan your day . ')
        
        
    elif 'headlines' in chat:
        webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
        talk('Here are some headlines from Times of India, happy reading')
        
        
    elif 'search' in chat:
        chat = chat.replace('search', '')
        print(chat + 'good')
        webbrowser.open_new_tab(chat)
        
    elif 'youtube' in chat:
        webbrowser.open_new_tab("https://www.youtube.com/")
        talk('Youtube is now open, enjoy')
        
    elif 'google' in chat:
        webbrowser.open_new_tab("https://www.google.com/")
        talk('Google is now open, enjoy')
        
    elif 'gmail' in chat:
        webbrowser.open_new_tab("https://www.gmail.com/")
        talk('gmail is now open, enjoy')

        
    elif 'meaning of' in chat:
        chat = chat.replace('what is the', '')
        chat = chat.replace('meaning of', '')
        means = wikipedia.summary(chat, 1)
        talk(means)
        print(chat)
        
    elif 'capital' in chat:
        app_id = '5X639U-WAP7U9827U'
        client = wolframalpha.Client(app_id)
        res = client.query(chat)
        ans = next(res.results).text
        talk(ans)
        print(ans)
        
        
    elif  "where is" in chat:
        chat = chat.replace("where is", "" )
        location_url = 'https://www.google.co.in/maps/place/' + chat
        talk("Hold on Rohan, I will show you where " + chat + " is.")
        print("Hold on Rohan, I will show you where " + chat + " is.")
        webbrowser.open_new_tab(location_url)


    elif "calculate" or "+" or "-" or "*" or "/" in chat:
        app_id = '5X639U-WAP7U9827U'
        client = wolframalpha.Client(app_id)
        math_res = client.query(chat)
        math_ans = next(math_res.results).text
        print("= " + math_ans)    


    elif 'weather of' or 'whats the weather like in' in chat:
        global listening
        
        API_URL = "http://api.openweathermap.org/data/2.5/weather?";
                
        API_KEY = "f13e951b419a4489bbb36891974f5443"
        
        if "weather of" in chat:
            location = chat.replace("weather of","")
            
        else:
            location = chat.replace("whats the weather like in","")
            complete_url =  API_URL + "appid=" + API_KEY + "&q=" + location
        
        js = requests.get(complete_url).json()
        
        if js["cod"] == "404":
            talk("sorry could not find the location you asked for")
            print("sorry could not find the location you asked for \n")
            
        else:

            weather = js["main"]
            current_tempratureK = weather["temp"]
            current_humidity = weather["humidity"]
            weather_description = js["weather"][0]["description"]
            current_tempratureC = round(current_tempratureK - 273.15)
            
            talk("temprature in celsius unit is " +
                 str(current_tempratureC) + 
                 "\n humidity in percentage is " + 
                 str(current_humidity) + 
                 "\n currently " + 
                 str(weather_description))
            
            print("temprature in celsius unit is " +
                 str(current_tempratureC) + 
                 "\n humidity in percentage is " + 
                 str(current_humidity) + 
                 "\n currently " + 
                 str(weather_description))
            
            
             
    else:
        talk('pardon me, can you please repeat that again.')
        print('pardon me, can you please repeat that again.')
        

