import requests
from nltk.tokenize import word_tokenize
import unicodedata
import pickle
import re

response = requests.get("https://www.gutenberg.org/files/58410/58410-0.txt")
data =response.text.lower() 

with open("nltk_tokenize.pkl", "wb") as f:
    write_down = word_tokenize(data)
    pickle.dump(write_down, f)

with open("normal_tokenize.pkl", "wb") as f:
    write_down = [re.sub(r'\W+', '', i) for i in data.split()]
    pickle.dump(write_down, f)