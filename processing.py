import re 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import pandas as pd

def tokenize_text(text):
    return word_tokenize(text)
def remove_characters(text):
    if isinstance(text, str):
        return re.sub(r'[^\w\s]', '', text)
    else:
        return text

def remove_stopwords(text):
    if isinstance(text, list):
        stop_words = set(stopwords.words('english'))
        return [word for word in text if word.lower() not in stop_words]
    


def remove_stopwords2(text):
    if not isinstance(text, list):
        raise ValueError("Input should be a list of words")
    
    stop_words = set(stopwords.words('english'))
    return [word for word in text if word.lower() not in stop_words]

    
    
def perform_stemming(text):
    if isinstance(text, list):
        stemmer = PorterStemmer()
        return [stemmer.stem(word) for word in text]

def perform_lemmatization(text):
    if isinstance(text, list):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word) for word in text]
    

def convert_to_lowercase(text):
    if isinstance(text, str):
        return text.lower()
    else:
        return text

def remove_emojis(text):
    if isinstance(text, str):
        emoji_pattern = re.compile("["
                                   u"\U0001F600-\U0001F64F"  # emoticons
                                   u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                                   u"\U0001F680-\U0001F6FF"  # transport & map symbols
                                   u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                                   "]+", flags=re.UNICODE)
        return emoji_pattern.sub(r'', text)
    else:
        return text
    

def remove_extra_spaces(text):
    if isinstance(text, str):
        return re.sub(' +', ' ', text)
    else:
        return text

def remove_numbers(text):
    if isinstance(text, str):
        return re.sub(r'\d+', '', text)
    else:
        return text
def remove_users(text):
    if isinstance(text, str):
        return re.sub(r'@\S+', '', text)
    else:
        return text
    
def remove_hastags(text):
    if isinstance(text, str):
        return re.sub(r'#\S+', '', text)
    else:
        return text

def remove_links(text):
    if isinstance(text, str):
        return re.sub(r'http\S+', '', text)
    else:
        return text

def preprocess_text(text):
    text = remove_links(text)
    text =remove_hastags(text)
    text = remove_characters(text)
    text =tokenize_text(text)
    text = remove_stopwords(text)
    text = perform_stemming(text)
    text = perform_lemmatization(text)
    text = remove_emojis(text)
    text = remove_extra_spaces(text)
    text = remove_numbers(text)
    return ' '.join(text)