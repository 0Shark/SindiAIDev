# HomeBuddy
<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/banner.jpg" width="100%">

#### Developed by: Juled Zaganjori and Elmer Dema
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)
[![HomeBuddy.ml](https://img.shields.io/badge/Web-HomeBuddy.ml-blue)](https://homebuddy.ml)
[![GitHub language count](https://img.shields.io/github/languages/count/0Shark/SindiAIDev)]()

Sindi is a natural language AI assistant that doesn’t only play music for you but it can also chat with you, tell you jokes and more. 
It doesn't matter how you ask the question Sindi will always understand what you mean unless the feature is not available.
Here is a list of the features Sindi has right now:
  - :speaking_head: Speak feature: *numbers and text* 
  - :right_anger_bubble: Chat features: *Hello, Who are you?, Tell a joke, Surname, Name, Thanks, full birthday, age (Sindi will know if you lie about your age)*
  - :sun_behind_rain_cloud: Weather features: *What's the weather like?*
  - :musical_note: Music features: *What genres of music do I listen?, Play music, Play rock music, Play custom music*
  - :control_knobs: Music controls: *Play, pause/continue, volume, mute/unmute, replay*
  - :red_circle: Exit app
  - :speech_balloon: Sindi will know if you are angry, neutral or happy based on your input

Current version features:
[YT Video](https://www.youtube.com/watch?v=gRr3pBE1pZ4)

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

<img src="https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/web.png" width="700">

We created HomeBuddy to be easily accessible by the users and serve as registration domain for all users. The website also includes log in using your face with the face_recognition module, but it won't work on the web due to hosting limitations, so you can still try it out by downloading the website here:

### [HomeBuddy.ml - Files](https://drive.google.com/file/d/12X0-BNVl4Q2d9qFQWHEfkTESfvOw56mW/view?usp=sharing)

If you want to check the HomeBuddy.ml code download the files from the [Google Drive link](https://drive.google.com/file/d/12X0-BNVl4Q2d9qFQWHEfkTESfvOw56mW/view?usp=sharing) and extract the files.

1) Firstly you need to have a local server running (for exp. WAMP)

2) After that you need to import the *database.sql* file into your local database managment framework (for exp. PhpMyAdmin)
#### Unessential procedure
To use the face_recognition features you need to install the python modules on requirements.txt.
```sh
cd YOURDIRECTORY
pip install -r requirements.txt
```
After the modules have been installed you can head over to localhost/homebuddy/ on your webbrowser.

#### [HomeBuddy.ml](https://homebuddy.ml)

- We hosted the website on 000webhost and aquired a free domain from Freenom
- The website is protected by CloudFlare security and posses a SSL certificate

## Installation
#### Before installation please make sure you are registered on the [web](https://homebuddy.ml) and you downloaded your data!
#### Sindi uses your custom preferences data to respond to you. 
SindiAI is built in [Python 3.6.6](https://www.python.org/downloads/release/python-366/) so make sure you have it installed together with *pip*
 
Next you need to clone the repository or just [download](https://github.com/0Shark/SindiAIDev/archive/main.zip) it.

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

NOTE: You can also install Sindi directly on your main Python installation but it may lead to small errors.

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

If you are asked to allow access to Firewall please do so.

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_7.png?raw=true)

And head over to 127.0.0.1:8000 on any web browser, or local ip of pc to use on other devices on your local network. *Example: 192.168.1.2:8000*

![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_9.png?raw=true)

Make sure you are registred on the [HomeBuddy](https://homebuddyweb.000webhostapp.com) website and you got your FaceHash together with your json data file. 
Your data should be located on */sindiai/users/data/* 

![Error](https://raw.githubusercontent.com/0Shark/SindiAIDev/main/screenshots/Screenshot_50.png?raw=true)

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
| <img src="https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_38.png" width="100%"> | <img src="https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_39.png" width="100%"> | <img src="https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_40.png" width="100%"> |

We have manually trained the app with nearly 300 sentences, labelling each type of data. 
![Error](https://github.com/0Shark/SindiAIDev/blob/main/screenshots/Screenshot_41.png?raw=true)


### Audio files

Sindi has a decent amount of speech audio generated with play.ht and music genres that can be modified to your preferences.
Make sure you add your own music files on the *sindiai/music/* directory. 

| Type | Items |
| ------ | ------ |
| text | 42 |
| number | 29 (audio files used to create other numbers) |
| jokes | 8 |
| months | 12 |
| music | 10 genres (where you can store your music)|

### Our development board, where we organized all of our tasks
[Trello Board](https://trello.com/b/AIOfJUvG/asef-2021-development-board)

### Todos (Dettailed version can be found on Trello board)

 - More chat functions :scroll:
 - Add Night Mode :dark_sunglasses:
 - Speech recognition :speaking_head:
 - Activate on call (Hey Sindi)
 - Play videos :film_strip:
 - Webdriver integration for searching :mag_right:

License
----
Copyright 2021 HomeBuddy.ml

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
