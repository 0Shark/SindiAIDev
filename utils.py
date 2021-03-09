from os import path, listdir, _exit  # Path, directory listing and exit
from wit import Wit           # API request
import json                   # Data extraction
from datetime import date     # Date
from random import randint    # Random index
from pygame import mixer      # Audio output
from pyowm import OWM         # Weather
from time import sleep        # Exit timer
import webbrowser


def openWebUI():
    url='127.0.0.1:8000'
    webbrowser.get('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s').open(url)


# Initiate mixer - used in audio functions
mixer.init()

# Wit
enableWitOutput = True  # True if you want to see Wit API response sent by our bot
access_token = "IYIKWAHYLSFGUGI3CM3SRVF4MBM2GQ7C"
client = Wit(access_token)

# OpenWeather  (2 keys in case limit is exceeded)
weatherAPI_token1 = "a1bdf2e4609febbedaf0fcc823e3d527"
weatherAPI_token2 = "44edc82d5c54a7d0cd68aec1904e810e"


# Music variables with deafult values
m_Name = "playing"
m_Cover = "static/covers/custom.png"
m_Genre = "No music"

try:
    mgr = OWM(weatherAPI_token1)
except Exception:
    mgr = OWM(weatherAPI_token2)

# Transcripts
transcript_path = "voice/transcript.json"
with open(transcript_path) as json_file:
    transcript = json.load(json_file)


openWebUI()


# Play audio responding to transcript (text)
def speak(text):
    audio_playing = mixer.music.get_busy()      # Checking if audio channel is playing audio
    while audio_playing:
        audio_playing = mixer.music.get_busy()
        continue

    mixer.music.unload()
    voice_path = transcript[text]
    mixer.music.load(voice_path)
    mixer.music.play()

# Convert tuples when response is a mix of strings and intigers ex. "Hello" + name + "!"
def convertTuple(tup):
    res = ''.join(tup)
    return res


# Get the highest confidence intent
def first_intent_name(intents):
    val = intents[0]['name']
    if not val:
        return None
    return val


# Get a certain entity
def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val


# Get a certain trait
def first_trait_value(traits, trait):
    if trait not in traits:
        return None
    val = traits[trait][0]['value']
    if not val:
        return None
    return val


# Turn nr to month using given index
def getMonth(month_nr):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    return months[month_nr - 1]


# Formatting birthday to string
def getBirthday(bday):
    date = bday.split('-')
    Y = date[0]
    M = date[1]
    M = int(M)
    D = date[2]
    msg = D + " of " + getMonth(M) + " " + Y
    speak(D)
    speak(getMonth(M))
    speakNumber(Y)

    return convertTuple(msg)


# Speak given number
def speakNumber(num):
    num = int(num)
    if num<0:
        speak("-")
        num = abs(num)
        num = str(num)
        speak(num)
    elif num==0:
        speak(num)
    elif num<=19 and num>=0: # Simple number
        speak(str(num))
    elif num<100 and num>=20: # Mixed number
        speak(str(int(num/10)*10))
        speak(str(num%10))
    elif num>1000: # Year
        temp = num%100  # Second half of year
        x = num/100 # First half of year
        x = int(x)
        if x==20:
            speak("2000")
        else:
            speak(str(int(x/10)*10))
            speak(str(x%10))
        num = num % 100
        y = str(int(num/10)*10)
        if y != "0":
            if temp<=19:
                speak(str(temp))
            else:
                speak(str(int(temp/10)*10))
                speak(str(temp%10))
        else:
            if temp<=19:
                speak(str(temp))
            else:
                speak(str(int(temp/10)*10))
                speak(str(temp%10))

# Calculate age from birthday given on data.json
def calAge(bday):
    born = bday.split('-')
    today = date.today()
    today = str(today)
    today = today.split('-')
    Y = today[0]
    Y = int(Y)
    M = today[1]
    M = int(M)
    D = today[2]
    D = int(D)
    Yb = born[0]
    Yb = int(Yb)
    Mb = born[1]
    Mb = int(Mb)
    Db = born[2]
    Db = int(Db)
    return Y - Yb - ((M, D) < (Mb, Db))


# Get genres from data.json
def get_music_genres(genres):
    msg = ""
    last = len(genres)
    genres.pop(last - 1)
    for x in genres:
        msg += x + ","
    return msg


# Recommend random music genre from given genres in data.json
def recommend_random_music(genres):
    global m_Name
    global m_Cover
    global m_Genre
    last = len(genres)
    genres.pop(last - 1)
    last = len(genres)
    index = randint(0, last - 1)
    genre = genres[index]
    response = genre
    file = get_music_file(genre)
    filename = file.split('.') 
    m_path = 'music/' + genre + '/' + file
    ignore = 'music/' + genre + '/DELETEME.txt'
    if path.exists(m_path) and m_path != ignore:
        speak("Playing")
        speak(genre)
        speak("music for you")
        play_music(m_path)
        m_Genre = genre
        m_Name = filename[0] 
        m_Cover = "static/covers/" + genre + ".png"
        response = genre + " music"
    else:
        speak("Sorry this music directory is empty!")
        response = genre + " music is not possible"
    return response


# Recommend music from given genre on input
def recommend_music(entity_value):
    global m_Name
    global m_Cover
    global m_Genre
    genre = entity_value
    file = get_music_file(genre)
    m_path = 'music/' + genre + '/' + file
    ignore = 'music/' + genre + '/DELETEME.txt'
    filename = file.split('.') 
    if path.exists(m_path) and m_path != ignore:
        speak("Playing")
        speak(genre)
        speak("music for you")
        play_music(m_path)
        m_Genre = genre
        m_Name = filename[0] 
        m_Cover = "static/covers/" + genre + ".png"
        response = genre + " music"
    else:
        speak("Sorry this music directory is empty!")
        response = genre + " music is not possible"
    return response


# Get random music file on genre folder
def get_music_file(genre):
    f_path = 'music/' + genre + '/'
    if listdir(f_path):
        playlist = listdir(f_path)
        index = randint(0, len(playlist) - 1)
        music_path = playlist[index]
        return music_path
    else:
        return False


# Play music with path m_path
def play_music(m_path):
    audio_playing = mixer.music.get_busy()  # Checking if audio channel is playing audio
    while audio_playing:
        audio_playing = mixer.music.get_busy()  # Waiting until audio has stopped
        continue
    mixer.music.unload()
    mixer.music.load(m_path)
    mixer.music.play()


# Music controls with pygame.mixer functions
def stop_music():
    mixer.music.unload()
    mixer.music.stop()


def replay_music():
    mixer.music.rewind()


def pause_music():
    mixer.music.pause()


def continue_music():
    mixer.music.unpause()


def lower_volume():
    mixer.music.set_volume(0.5)


def increase_volume():
    mixer.music.set_volume(1)


def mute_volume():
    mixer.music.set_volume(0)


def unmute_volume():
    mixer.music.set_volume(0.7)


# Random approve response from list
def approve_response():
    responses = ['Sure!', 'Ok.', 'Sure thing.', 'Yes Sir!', 'Done!']
    index = randint(0, len(responses) - 1)
    return responses[index]

# Check if music is playing and get values if it's called from server.py
def music_playing():
    global m_Name
    global m_Cover
    global m_Genre
    audio_playing = mixer.music.get_busy()
    arr = ["static/covers/custom.png", "No music", "Playing"]      # Checking if audio channel is playing audio
    if audio_playing:
        arr = [m_Cover, m_Genre, m_Name]
    else:
        arr = ["static/covers/custom.png", "No music", "Playing"] 
    return arr



# Tell a random joke corresponding to joke id
def tell_joke():
    jokes = ['j1','j2','j3','j4','j5','j6','j7','j8']
    index = randint(0, len(jokes) - 1)
    speak(jokes[index])
    return ":D"


# Giving a response
def give_response(wit_output, u_data):
    # Getting user data from data.json
    data = u_data[0]
    name = data['Name']
    surname = data['Surname']
    bday = data['Birthday']
    global city
    city = data['Location']
    music = data['Music']
    music_genres = music.split(",")

    # Print Wit response
    if enableWitOutput:
        print("Wit API:")
        print(wit_output)

    # Getting intents, entities and traits from API response
    # And classifying according to intent name or trait (ex: question, greeting, bye, thanks)
    # If there is no response it means our bot didn't understand the utterance
    # So we set understood as False and we will return None
    understood = False
    if wit_output['intents']:
        intents = wit_output['intents']
        intent_type = first_intent_name(intents)
        understood = True
    if wit_output['entities']:
        entities = wit_output['entities']
        entity_age_of_person = first_entity_value(entities, 'wit$age_of_person:age_of_person')
        entity_music_genre = first_entity_value(entities, "music_genre:music_genre")
        entity_user_playlist = first_entity_value(entities, "user_playlist:user_playlist")
        understood = True
    if wit_output['traits']:
        traits = wit_output['traits']
        trait_greeting = first_trait_value(traits, 'wit$greetings')  # Values: true
        trait_thanks = first_trait_value(traits, 'wit$thanks')  # Values: true
        trait_bye = first_trait_value(traits, 'wit$bye')  # Values: true
        trait_sentiment = first_trait_value(traits, 'wit$sentiment')  # Values: positive, neutral, negative
        trait_question = first_trait_value(traits, 'question')  # Value: true, false
        understood = True
    else:
        return "Uh... I didn't get that."

    if understood:
        if intent_type == 'creator_related':
            return "I was created by Juled Zaganjori and Elmer Dema."
        elif intent_type == 'greeting_related' and trait_greeting == 'true':
            msg = "Hello there " + name + "!"
            speak("Hello there!")
            return convertTuple(msg)
        elif intent_type == 'goodbye_related' and trait_bye == 'true':
            msg = "Goodbye " + name + "!"
            speak("Goodbye!")
            return convertTuple(msg)
        elif intent_type == 'name_related' and trait_question == 'true':
            msg = "Your name is " + name + "."
            speak("Your name is written right here.")
            return convertTuple(msg)
        elif intent_type == 'surname_related' and trait_question == 'true':
            msg = "Your surname is " + surname + "."
            speak("Your surname is written right here.")
            return convertTuple(msg)
        elif intent_type == 'sindi_related':
            speak("I'm your personal assistant. I'm going to help you out when you need me and cheer you up with music, videos and jokes.") # Videos coming soon
            return "I'm your personal assistant. I'm going to help you out when you need me and cheer you up with music and jokes."
        elif intent_type == 'thanks_related' or trait_thanks == 'true':
            speak("No problem!")
            return "No problem! :)"
        elif intent_type == 'bday_related':
            speak("You were born on") # Other part of sentence is played on getBirthday()
            msg = "You were born on " + str(getBirthday(bday))
            return convertTuple(msg)
        elif intent_type == 'age_related':
            if trait_question == 'true':

                speak("You are")
                speakNumber(calAge(bday))
                speak("years old")

                msg = "You are " + str(calAge(bday)) + " years old."
                return convertTuple(msg)
            elif trait_question == 'false':
                age = entity_age_of_person.split(" ")
                age = age[0]
                age = int(age)
                if age != calAge(bday):

                    speak("Don't be silly I know you are")
                    speakNumber(calAge(bday))

                    msg = "Don't be silly I know you are " + str(calAge(bday))
                    return convertTuple(msg)
                elif age == calAge(bday):
                    speak("Yes you are.")
                    return "Yes you are."
        elif intent_type == 'weather_related':
            observation = mgr.weather_at_place(city)
            w = observation.get_weather()
            state = w.get_status()
            wind_data = w.get_wind()
            humidity = w.get_humidity()
            temp_data = w.get_temperature('celsius')

            speak("The weather is looking")
            speak(state)
            speak("with air temperature")
            speakNumber(int(temp_data['temp']))
            speak("degrees Celsius")
            speak("The wind speed is")
            speakNumber(int(wind_data['speed']))
            speak("mph")
            speak("and humidity is")
            speakNumber(int(humidity))
            speak("percent")

            msg = "The weather is looking with " + state + " with air temperature " + str(int(temp_data['temp'])) + " degrees Celcius. The wind speed is " + \
                  str(int(wind_data['speed'])) + " mph" + " and humidity is " + str(humidity) + "%"
            return convertTuple(msg)
        elif intent_type == 'expression_related':
            if trait_sentiment == "positive":
                msg = ";D"
                return msg
            elif trait_sentiment == "negative":
                msg = ":("
                return msg
            elif trait_sentiment == "neutral":
                msg = ":)"
                return msg
        elif intent_type == 'tell_joke':
            return convertTuple(tell_joke())
        elif intent_type == 'music_related':
            if trait_question == 'true':
                msg = "You like listening to ", get_music_genres(music_genres), " music genres."    # Need to generate audio file
                return convertTuple(msg)
        elif intent_type == 'music_recommend':
            if not entity_music_genre and not entity_user_playlist:
                genre = recommend_random_music(music_genres)
                msg = "Playing ", genre, " music for you now."
                return convertTuple(msg)
            elif entity_music_genre:
                msg = "Playing ", recommend_music(entity_music_genre), " for you now."
                return convertTuple(msg)
            elif entity_user_playlist == 'user_playlist':
                msg = "Playing ", recommend_music('custom'), " for you now."
                return convertTuple(msg)
        elif intent_type == 'pause':
            pause_music()
            return approve_response()
        elif intent_type == 'unpause':
            continue_music()
            return approve_response()
        elif intent_type == 'stop':
            stop_music()
            resp = approve_response()
            speak(resp)
            return resp
        elif intent_type == 'replay':
            replay_music()
            return approve_response()
        elif intent_type == 'lower_volume':
            lower_volume()
            return approve_response()
        elif intent_type == 'increase_volume':
            increase_volume()
            return approve_response()
        elif intent_type == 'mute':
            mute_volume()
            return approve_response()
        elif intent_type == 'unmute':
            unmute_volume()
            return approve_response()
        elif intent_type == 'exit_app':
            speak("I'm going dark to be woken greater then ever. Goodbye!")
            sleep(7)
            _exit(0)
    else:
        return None


# Gets input from server.py from Form
def giveInput(user_input, facehash):
    data_path = "users/data/" + facehash + ".json"
    with open(data_path) as json_file:
        data = json.load(json_file)

    if user_input == '':
        user_input = "NULL"  # Error from wit for empty values so we set deafult value NULL
    wit_output = client.message(user_input)
    response = give_response(wit_output, data)
    if response is not None:
        return response
    else:
        speak("I didn't get that")
        return "Uh... I didn't get that."

'''
# Testing
data_path = "users/data/Mshsp.json"
with open(data_path) as json_file:
    data = json.load(json_file)

while True:
    user_input = input(">>>")
    if user_input == '':
        user_input = "NULL"  # Error from wit for empty values
    wit_output = client.message(user_input)
    print(give_response(wit_output, data))
'''
