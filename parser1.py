import requests
import re

url = 'https://sealydoc.com/'
response = requests.get(url)
text_data = response.text

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('stopwords')
nltk.download('punkt')


# Clear text
text = re.sub(r'\<[^>]*\>','',text_data)
#print(text)
# Tokenization
tokens = word_tokenize(text)

# Removing stopwords and stemming
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
cleaned_tokens = [stemmer.stem(word.lower()) for word in tokens if word.lower() not in stop_words]

import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Create a word cloud
wordcloud = WordCloud(width=800, height=400).generate(' '.join(cleaned_tokens))

# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
