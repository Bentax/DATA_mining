import re
import nltk
import emoji
import unicodedata
import contractions
import inflect
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from pymystem3 import Mystem
from string import punctuation
from wordcloud import WordCloud
nltk.download('popular')
nltk.download('stopwords')
nltk.download('punkt')

# Функция для очистки текста
def clean_text(input_text):    
    # HTML-теги: первый шаг - удалить из входного текста все HTML-теги
    clean_text = re.sub('<[^<]+?>', '', input_text)    
    # URL и ссылки: далее - удаляем из текста все URL и ссылки
    clean_text = re.sub(r'http\S+', '', clean_text)
    # Эмоджи и эмотиконы: используем собственную функцию для преобразования эмоджи в текст
    #clean_text = emojis_words(clean_text)    
    # Приводим все входные данные к нижнему регистру
    clean_text = clean_text.lower()
    # Так как все данные теперь представлены словами - удалим пробелы
    clean_text = re.sub('\s+', ' ', clean_text)
    # Преобразование символов с диакритическими знаками к ASCII-символам: используем функцию normalize из модуля unicodedata и преобразуем символы с диакритическими знаками к ASCII-символам
    #clean_text = unicodedata.normalize('NFKD', clean_text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    # Разворачиваем сокращения: текст часто содержит конструкции вроде "don't" или "won't", поэтому развернём подобные сокращения
    #clean_text = contractions.fix(clean_text)
    #clean_text = re.sub('[^a-zA-Z0-9\s]', '', clean_text)
    # Убираем специальные символы и цифры: избавляемся от всего, что не является "словами"
    clean_text = re.sub('[^а-яА-Я\s]', '', clean_text)
    # Записываем числа прописью: 100 превращается в "сто" (для компьютера)
    '''
    temp = inflect.engine()
    words = []
    for word in clean_text.split():
        if word.isdigit():
            words.append(temp.number_to_words(word))
        else:
            words.append(word)
    clean_text = ' '.join(words)
    '''
    # Стоп-слова: удаление стоп-слов - это стандартная практика очистки текстов
    tokens = word_tokenize(clean_text,language='russian')
    stop_words = set(stopwords.words('russian'))
    tokens_ = [token for token in tokens if token not in stop_words]
    clean_text = ' '.join(tokens_)
    # Знаки препинания: далее - удаляем из текста все знаки препинания
    clean_text = re.sub(r'[^\w\s]', '', clean_text)
    # И наконец - возвращаем очищенный текст
    return clean_text

# Функция для преобразования эмоджи в слова
def emojis_words(text):    
    # Модуль emoji: преобразование эмоджи в их словесные описания
    clean_text = emoji.demojize(text, delimiters=(" ", " "))    
    # Редактирование текста путём замены ":" и" _", а так же - путём добавления пробела между отдельными словами
    clean_text = clean_text.replace(":", "").replace("_", " ")    
    return clean_text

import pandas as pd

data = pd.read_csv('Mesto.csv')
data.columns = ['ID', 'DATE', 'AGE', 'COUNTRY', 'PROJ', 'FROM', 'FROM1', 'ABOUT', 'PROF', 'PROF1', 'VALUE', 'VALUE1', 'L_FOR', 'L_FOR1', 'TYPE', 'ROLE']
data = data.dropna(subset=['ABOUT','TYPE'])
#reset index of DataFrame
data = data.reset_index(drop=True)
print(data.shape[0])
code_data = data['ABOUT'].values.astype('U')
text = ''.join(code_data)
print(len(text))
c_text = clean_text(text)
print(len(c_text))
#23305
#8219755
#6227966
