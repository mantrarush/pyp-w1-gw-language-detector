# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES
from string import punctuation
"""
        languages_words = {
            "Spanish": 90,
            "German": 150
        }
        
        text_occurrences = {
            "Spanish": 45,
            "German": 100
        }
        
        stats = {
            "Spanish": "50%",
            "German": "66%"
        }
    """
def calculate_percentages(text_occurrences): #Gives the statistics of matches with each language
    total_words = {lang["name"]: len(lang["common_words"]) 
                   for lang in LANGUAGES}
    stats = {}
    for key, value in text_occurrences.iteritems():
        num = (float(text_occurrences[key]) / float(total_words[key])) * 100
        stats[key] = str(round(num, 2)) + "%"
    
    return stats
    
 # removes punctuations from the text 
def clean_words(text):
   return ''.join(c for c in text if c not in punctuation)

   
def most_common(text): # finds the most common word that occurs in the text 
    d = dict()
    wordlist = clean_words(text).split() #splits per whitespace
    for word in wordlist:
        word = word.lower() #so that cat and Cat evaluate to the same word
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    max_value = 0
    for key, value in d.items():
        #print key, value
        if value >= max_value:
            max_value = value
            word = key
            
    return word  #returns the most common word found 
    """Returns the detected language of given text.
        >break the text into words 
        >iterate over the words, check whether each word is in the list
        >"This is a cat". check whether "this" is in the english set 
    """
def detect_language(text, languages=LANGUAGES):
    wordlist = clean_words(text).split()
    counters = {d['name']: 0 for d in languages}
    for lang_dict in languages:
        for word in wordlist: 
            if word in lang_dict["common_words"]:
               counters[lang_dict["name"]] += 1
    max_value = 0 
    for key, value in counters.items():
        if value >= max_value:
            max_value = value
            to_return = key
            
    return to_return
    

        