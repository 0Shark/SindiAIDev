# from face_recognition import load_image_file
import json
from utils import face_exists, give_response
# from face_recon import webcam_detection
from wit import Wit

# Wit access token
access_token = "IYIKWAHYLSFGUGI3CM3SRVF4MBM2GQ7C"
# Welcoming message
print("Sindi: Hello there I'm Sindi, your personal AI assistant. \n"
      "Sindi: Before we start I need you to insert your FaceHash.")
known_face = False
while not known_face:
    facehash = input(">>>")
    # Let's check if facehash exists on users/faces
    known_face = face_exists(facehash)

print("Sindi: Ok show your face in front of your camera so I can identify if this is really you!")
# Get json data of user
data_path = "users/data/" + facehash + ".json"
with open(data_path) as json_file:
    data = json.load(json_file)

# print(json.dumps(data, indent=4))
# Load face image
known_face = load_image_file(known_face)
# Get display name from users/data
name = data[0]['Name']
surname = data[0]['Surname']
display_name = name + " " + surname

# Start webcam detection
if (webcam_detection(known_face, display_name)):
    # Connect to wit
    client = Wit(access_token)
    #print("SERVER: CONNECTED")

    print("Sindi: Hello", name + "!")

    speech_active = False
    '''
    # COMING SOON
    print("Would you like to activate TTS (Text-To-Speech)? [Yes/No]\n"
          "NOTE: This is still a BETA feature and may slow down response time.")
    choice = input(">>>")
    choice.upper()
    if choice == "YES":
        speech_active = True
    elif choice == "NO":
        speech_active = False
    else:
        print("Sorry this is a Yes or No question.")
    '''
    if speech_active:
        print("I'm now activating speech recognition.\n"
              "You can now talk to me using your microphone!")
    else:
        active = True
        while active:
            user_input = input(">>>")
            wit_output = client.message(user_input)
            give_response(wit_output, data)

