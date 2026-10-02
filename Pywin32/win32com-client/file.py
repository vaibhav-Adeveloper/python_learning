import time
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    time.sleep(1)
    speak.SpeaK(str)

if __name__ == '__main__':
    speak("You are my best friend saurav. chuut pai chumma dai chuut maari waalai")
    # speak("Happy Birthday Praful Bhhai")