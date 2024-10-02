# Импорт необходимых библиотек
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

file_path = 'Стартапы.csv'
df = pd.read_csv(file_path)

# Обработка текста: выбор столбца "Описание" и объединение всех текстов в одну строку
text = " ".join(description for description in df["Описание"].dropna())

# Определение стоп-слов
stopwords = {'а', 'в', 'на', 'с', 'или', 'и', 'по', 'для', 'от', 'из', 'не', 'это', 'мы', 'о', 'что', 'за', 'можно', 'как', 'который', 'до', 'and', 'the', 'to', 'with', 'for'}

# Создание облака слов
wordcloud = WordCloud(stopwords=stopwords, background_color='white', width=800, height=400).generate(text)

# Визуализация облака слов
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Облако слов для столбца 'Описание'")
plt.show()
