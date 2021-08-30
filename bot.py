import datetime
import random

def get_ans(req):
    req = req.lower()

    if 'hi' in req or 'hello' in req:
        return "Hello!"
    elif 'what' in req and 'time' in req:
        now = datetime.datetime.now()
        return "It's %s:%s" % (now.hour, now.minute)
    elif 'how' in req and 'you' in req:
        return "I'm doing great!"
    elif 'weather' in req:
        return "It's such a great sunny day!"
    elif 'temperature' in req:
        return "It's about 15 degrees."
    elif 'color' in req:
        return "It's blue."
    elif 'university' in req or 'itmo' in req:
        return "ITMO university!"
    else:
        return "It's a pleasure to meet you!"

sentences = ["How are you?", "What are you doing now"
            "Good to see you!", 
            "I'm always here.",
            "Ask me anything.",
            "What a beautiful day!",
            "Hello!"
            ]

def chatting():
    return random.choice(sentences)