import re
import long_responses as long
import random
import intents

def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
    message_certainty = 0
    has_required_words = True

    # Counts how many words are present in each predefined message
    for word in user_message:
        if word in recognised_words:
            message_certainty += 1

    # Calculates the percent of recognised words in a user message
    percentage = float(message_certainty) / float(len(recognised_words))

    # Checks that the required words are in the string
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break

    # Must either have the required words, or be a single response
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob_list = {}

    # Simplifies response creation / adds it to the dict
    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    # Responses -------------------------------------------------------------------------------------------------------
    # Required words are words that have to be in the users input in order for the response
    # Random responses from intent file is generated depending on what user says
    
    response(intents.greeting_intent[random.randint(1, len(intents.greeting_intent))], ['hello', 'hi', 'hey', 'yo'], single_response=True)
    response(intents.leaving_intent[random.randint(1, len(intents.leaving_intent))], ['bye', 'goodbye'], single_response=True)
    response(intents.wellness_intent[random.randint(1, len(intents.wellness_intent))], ['how', 'are', 'you', 'doing'], required_words=['how'])
    response(intents.thanks_intent[random.randint(1, len(intents.thanks_intent))], ['thank', 'thanks'], single_response=True)
    response('Thank you! I love you too', ['i', 'love', 'you'], required_words=['love', 'you'])
    

    # Longer responses --------------------------------------------------------------------------------------------------
    response(long.PURPOSE, ['what', 'is', 'your', 'purpose'], required_words=['your', 'purpose'])
    response(long.PURPOSE, ['what', 'can', 'you', 'do'], required_words=['you', 'do'])
    response(long.TIME, ['what', 'time', 'is', 'it', 'right', 'now'], required_words=['time','now'])
    response(long.NOW, ['what', 'is', 'the', 'date', 'and', 'time'], required_words=['date', 'and','time'])
    response(long.WEATHER, ['what', 'is', 'the', 'weather', 'here'], required_words=['what', 'weather'])
    response(long.NAME, ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
    
    
    #calculates the highest probability for the response, and the highest one's response is returned
    best_match = max(highest_prob_list, key=highest_prob_list.get)
   

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


# Used to get the response
def get_response(user_input):

    #gets rid of all common punctuations, so just the words remain
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


while True:
    print('Bot: ' + get_response(input('You: ')))