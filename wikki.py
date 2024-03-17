import wikipedia
from translater import google_translate

def wiki(word):
    try:
        return google_translate(wikipedia.summary(word))
    
    except:
        return f"'{word}' topilmadi!"
    
