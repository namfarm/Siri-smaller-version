import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()
robot_brain = " "
robot_voice = pyttsx3.init()
voices = robot_voice.getProperty('voices')
robot_voice.setProperty('voices', voices[0].id)
while True:
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)
        print("Robot:.....")

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    if you == "":
        robot_brain = " I can't hear you, try again "
    elif "Siri" in you:
        robot_brain = "Hi, I'm Siri, ready to answer your question"
    elif "hello" in you:
        robot_brain = "hello Nam Farm"
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B, %d, %Y")
    elif " time " in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minute %S second")
    elif "president" in you:
        robot_brain = "Donal Trump"
    elif "pretty" in you:
        robot_brain = "Stop asking that question everyone knows you're pretty"
    elif "bye" in you:
        robot_brain = "GoodBye Nam Farm"
        print("Robot: " + robot_brain)
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "I'm fine thank you and you"
    print("Robot: " + robot_brain)
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
