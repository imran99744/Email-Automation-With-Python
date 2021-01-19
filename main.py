import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def get_info():
    try:
        with sr.Microphone() as source:
            print("listening...")
            voice = listener.listen(source)
            info = listener.recognize_google(voice)
            print(info)
            return info.lower()
    except:
        pass


def send_email(receiver, subject, message):

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("trying4402021@gmail.com", "22710202")
    email = EmailMessage()
    email["From"] = "trying4402021@gmail.com"
    email["To"] = receiver
    email["Subject"] = subject
    email.set_content(message)
    server.send_message(email)


email_list = {
    'lisa': 'mdimrn99@gmail.com',
    'mimi': 'jony99@gmail.com',
}


def get_email_info():
    talk("To whom you want to send email")
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk("What is the subject of your email")
    subject = get_info()
    talk("What is the text of your email")
    message = get_info()
    send_email(receiver, subject, message)
    talk("Hey IMRAN. Your email is sent")
    talk("Do you want to send more emails?")
    send_more = get_info()
    if 'yes' in send_more:
        get_email_info()


get_email_info()
