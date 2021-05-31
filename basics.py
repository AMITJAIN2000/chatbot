# Meet Pybot: your friend
import webbrowser
import nltk
import warnings
import wikipedia
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


warnings.filterwarnings("ignore")
import numpy as np
import random
import string

f = open('modules.txt', 'r', errors='ignore')
m = open('modules.txt', 'r', errors='ignore')
# checkpoint = "./chatbot_weights.ckpt"
# session = tf.InteractiveSession()
# session.run(tf.global_variables_initializer())
# saver = tf.train.Saver()
# saver.restore(session, checkpoint)

raw = f.read()
raw = raw
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is PyBot.", "My name is PyBot you can called me pi.", "Im PyBot :) ",
                 "My name is PyBot. and my nickname is pi and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("what is python ?", "what is python", "what is python?", "what is python.")
Basic_Ans = "Python is a high-level, interpreted, interactive and object-oriented scripting programming language python is designed to be highly readable It uses English keywords frequently where as other languages use punctuation, and it has fewer syntactical constructions than other languages."
Basic_Om = ("what is module", "what is module.", "what is module ", "what is module ?", "what is module?",
            "what is module in python", "what is module in python.", "what is module in python?",
            "what is module in python ?")
Basic_AnsM = ["Consider a module to be the same as a code library.",
              "A file containing a set of functions you want to include in your application.",
              "A module can define functions, classes and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use."]
Basic_R = ("who", "who is your mam")
Basic_AnsR = ["i am rupali bhartiya", "my rupali bhartiya"]
query = ("salman khan wikipedia")
bro = ("youtube")


# query_1= wikipedia.summary(query,sentences=2)
# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans


# Checking for Basic_QM
def basicM(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_Om:
        if sentence.lower() == word:
            return random.choice(Basic_AnsM)


# Checking for Basic_R
def basicR(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in Basic_R:
        if sentence.lower() == word:
            return random.choice(Basic_AnsR)


def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)




# Generating response
def response(user_response):
    found=0
    with open("modules.txt","r",encoding="utf8") as f:
        for i in f:
            m=i[0:len(user_response)].lower().strip()
            if m==user_response:
                result=i
                # engine.say(i[len(user_querry)+3: ])
                # engine.runAndWait()

                found=1
                break
        if found==0:
            try:
                result = wikipedia.summary(f"%{user_response}", sentences=2)
            except:
                result=f"{user_response} is not found in data base"
        return result


def chat(user_response):

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            return "You are welcome.."
        elif (basicM(user_response) != None):
            return basicM(user_response)
        elif (basicR(user_response) != None):
            return basicR(user_response)
        else:
            if (greeting(user_response) != None):
                return greeting(user_response)
            elif (user_response.find("your name") != -1 or user_response.find(
                    "who are you") != -1 or user_response.find("your name ") != -1 or user_response.find(
                    " your name ") != -1):
                return IntroduceMe(user_response)
            elif (basic(user_response) != None):
                return basic(user_response)
            else:
                # print("ROBO: ",end="")
                # print(response(user_response))
                return response(user_response)

    else:
        return "Bye! take care.."
