import pyttsx3

from basics import chat,Introduce_Ans
import random
####################### Python sound settings#############################
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

if __name__ == '__main__':
    x=1
    print(random.choice(Introduce_Ans))
    while x!=0:
        user_querry=input().lower().strip()
        result=chat(user_querry)
        print(result)
        engine.say(result)
        engine.runAndWait()

        x = int(input("Press 0 to exit"))






