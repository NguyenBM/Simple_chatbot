"""

This file returns long responses when a question that requiores one is prompted
This is also where all the longer functions will be held as well


"""

import random
import chatbot_functions as functions
from datetime import datetime

n = datetime.now()


# variables containing longer responses that will be returned to the user when promted 

PURPOSE = "I can perform simple calculations as of now, tell the time, the date, generate a random password for you and even tell the time!"
NOW = str(n)
TIME = "The time right now is currently " + str(n.time())
CITY_WEATHER = input('Hey there! My name is Robert, may I ask what city are you located in? ')
CITY_WEATHER += " weather"
WEATHER = functions.weather(CITY_WEATHER)
NAME = "My name is robert! It is good to meet you, what can I do for you today?"




# if the bot cannot recoginize what the user is saying then it will respond with a random response
def unknown():
    response = ["Could you please re-phrase that? ",
                "...",
                "I don\'t understand what you are saying, could you repeat that?",
                "What does that mean?",
                "I\'m sorry, could you say that again?"
                "I didn\'t quite get that."][random.randrange(5)]
    return response
    
    
    
    
    