import speech_recognition as sr

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Say something!")
        audio = r.listen(source)
        
        print("Processing...")
        sst=r.recognize_google(audio)
        print("You said: ", sst)
main()