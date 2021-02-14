# SindiAI
#### Project participating in ASEF 2021

Sindi is a natural language AI assistant that doesn’t only play music for you but it can also chat with you, tell you jokes and more. 
It doesn't matter how you ask the question Sindi will always understand what you mean unless the feature is not available.
Here is a list of the features Sindi has right now:
  - Speak feature: *numbers and text*
  - Chat features: *Hello, Who are you?, Surname, Name, Thanks, full birthday, age (Sindi will know if you lie about your age)*
  - Weather features: *What's the weather like?*
  - Music features: *What genres of music do I listen?, Play music, Play rock music, Play custom music*
  - Music controls: *Play, pause/continue, volume, mute/unmute, replay*
  - Exit app
  - Sindi will know if you are angry, neutral or happy based on your input

### Technologies used
##### On web
<p float="left">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/htmlcss.png" width="100">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/php.png" width="100">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/sql.png" width="100">
</p>

##### On SindiAI

<p float="left">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/python.png" width="100">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/flask.png" width="100">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/wit.png" width="100">
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/sql.png" width="100">
</p>

### Web | HomeBuddy website
We created HomeBoddy to be easily accesible by the users and serve as registration domain for all users. The website also includes log in using your face with the face_recognition module but it won't work on the web due to hosting limitations, so you can still try it out by downloading the website here:
[Google Drive link](https://drive.google.com/file/d/1IzaHphtCNDt0kwedOl_VFuy3xdYd7Fua/view?usp=sharing)
[Website](homebuddy.ml)

- We hosted the website on 000webhost and aquired a free domain from Freenom
- The website is protected by CloudFlare security and posses a SSL certificate

### Installation
SindiAI is built in [Python 3.6.6](https://www.python.org/downloads/release/python-366/) so make sure you have it installed together with *pip*
 
Next you need to clone the repository or just [download](https://github.com/0Shark/SindiAIDev/archive/main.zip) it 

```sh
git clone https://github.com/0Shark/SindiAIDev
```

After that you can change directory to there

```sh
cd /YOURFOLDER/sindiai/
```
We recommend creating a virtual environment to manage your modules more easily, in this case we used anaconda to create the environment like this:
```sh
conda create -n sindiai python==3.6.6
```
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_3.png?raw=true)

Now activate the environment:
```sh
conda activate sindiai
```
Now you can install all the required modules with this command:
```sh
pip install -r requirements.txt
```
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_4.png?raw=true)
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_5.png?raw=true)

After installing all the modules, make sure to have a MySQL local server running. In this case we are running Wamp(Windows, Apache, MySQL, and PHP).

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_36.png?raw=true)

Then you can run to create the database:
```sh
python create_db.py
```

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_6.png?raw=true)

After the database has been created you can start using SindiAI by running:
```sh
python server.py
```

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_8.png?raw=true)

If you are asked to allow acces to Firewall please do so.

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_7.png?raw=true)

And head over to 127.0.0.1:8000 on any web browser, or local ip of pc to use on other devices on your local network. *Example: 192.168.1.2:8000*

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_9.png?raw=true)

Make sure you are registred on the [HomeBuddy](https://homebuddyweb.000webhostapp.com) website and you got your FaceHash together with your json data file. And it should be located on */sindiai/users/data/* 

Then you can, 

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_10.png?raw=true)

### You are ready to chat with Sindi!
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_11.png?raw=true)

### Wit integration
The moment we send input to Sindi a chain of functions are activated. 
First we send the input to Wit where it is classified into intents, entities and traits.
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_14.png?raw=true)
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_13.png?raw=true)
| What are intents? | What are entities? | What are traits? |
| ------ | ----- | ----- |
| We have created these intents to classify the response | Entities detect certain objects in the user input (genre, age, date) | Traits help us detect a trait about in sentence (sntiment ex. happy) |
| ![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_38.png?raw=true) | ![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_39.png?raw=true) | ![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_40.png?raw=true) |

We have manually trained the app with nearly 300 sentences, labelling each type of data. 
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_41.png?raw=true)


### Audio files

Sindi has a decent amount of speech audio generated with play.ht and music genres that can be modified to your preferences.
Make sure you add your own music files on the *sindiai/music/* directory. 

| Type | Items |
| ------ | ------ |
| text | 42 |
| number | 29 (base numbers that serve to create 1000 more) |
| jokes | 8 |
| months | 12 |
| music | 10 genres |

### Todos

 - More chat functions
 - Add Night Mode
 - Speech recognition
 - Activate on call (Hey Sindi)
 - Play youtube videos

License
----

MIT
