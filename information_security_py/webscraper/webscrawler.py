# Web Scrawler

# Author: @andvsilva
# date 2021-11-08

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter
from icecream import ic
import snoop
import time

# define web scraler
@snoop
def start(url):
    
    wordlist = [] # to store the content of the site
    source_code = requests.get(url).text # get text from site
    
    soup = BeautifulSoup(source_code, 'html.parser')
    
    # Text in given web-page is stored under
    # the <div> tags with class <entry-content>
    for each_text in soup.findAll('h4', {'class': 'sk-card-title card-title'}):
        content = each_text.text
        
        words = content.lower().split()
        #ic(words)
        
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)
        
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$%^&*()_-=+{[}]|\;:"<>?/., '
        
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')
            
        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)
    

def create_dictionary(clean_list):
    word_count = {}
    
    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))
        
    c = Counter(word_count)
    
    top = c.most_common(10)
    print(top)
    
if __name__ == '__main__':
    start("https://scikit-learn.org/stable/")