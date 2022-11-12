"""
This file will perform the more advanced functions for the chatbot

"""
import math
from bs4 import BeautifulSoup
import requests 













# weather function, able to tell the weather when prompted by user (Try to give the user an option between faarenheit or celsius)
# Uses the bs4 python module which allows us for to grab the users input and search up the weather for the area and return it
def weather(city): 
    city=city.replace(" ","+")
    
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    
    soup = BeautifulSoup(res.text,'html.parser')   
    location = soup.select('#wob_loc')[0].getText().strip()  
    time = soup.select('#wob_dts')[0].getText().strip()       
    info = soup.select('#wob_dc')[0].getText().strip() 
    weather = soup.select('#wob_tm')[0].getText().strip()
     
    return "The weather in " + location + " at " + time + " is " + info + " " + weather + "°F"


def simple_calculator(user_input):
    pass


