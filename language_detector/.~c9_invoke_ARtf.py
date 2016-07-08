# -*- coding: utf-8 -*-
"""This is the entry point of the program."""

from .languages import LANGUAGES

def calculate_percentages(text_occurrences):
    """
        languages_words = {
            "Spanish": 90,
            "German": 150
        }
        
        text_occurrences = {
            "Spanish": 45,
            "German": 100
    for word in wordlist: 
        
        stats = {
            "Spanish": "50%",
            "German": "66%"
        }
    """
    total_words = {lang["name"]: len(lang["common_words"]) 
                   for lang in LANGUAGES}
    stats = {}
    for key, value in text_occurrences.iteritems():
        num = (float(text_occurrences[key]) / float(total_words[key])) * 100
        stats[key] = str(round(num, 2)) + "%"
    
    return stats
    

def most_common(text):
    pass
"""
    d = dict()
    wordlist = text.split()
    for word in wordlist:
        if word.lower() in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
    max_value = 0
    for key, value in d.iteritems():
        #print key, value
        if value >= max_value:
            max_value = value
            to_return = key
            
    return to_return    
"""

def detect_language(text, languages=LANGUAGES):

    wordlist = text.split()
    counters = {d['name']: 0 for d in languages}
 
    for lang_dict in languages:
        for word in wordlist: 
            if word in lang_dict["common_words"]:
               counters[lang_dict["name"]] += 1

    max_value = 0 
    for key, value in counters.iteritems():
        if value >= max_value:
            max_value = value
            to_return = key
            
    return to_return
    
"""
Solve with regexes (adjusting and/or adding tests might be needed for this)
Stats (What word is most common, percentage of languages etc etc)
"""
        