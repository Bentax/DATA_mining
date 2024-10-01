# Импорт необходимых библиотек
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import jaccard_score
import numpy as np

# Чтение .csv файла (замените на путь к вашему файлу)
file_path = 'Стартапы.csv'
df = pd.read_csv(file_path)

# Функция для очистки текста от спецсимволов и лишних пробелов
def clean_text(text):
    # Удаление спецсимволов, знаков препинания и приведение к нижнему регистру
    text = re.sub(r'[^\w\s]', ' ', text)  # Удаление всех символов, кроме букв, цифр и пробелов
    text = re.sub(r'\s+', ' ', text).strip()  # Замена нескольких пробелов на один
    text = text.lower()  # Приведение к нижнему регистру
    return text

# Очистка текста в столбцах "Описание" и "Ключевые слова"
df["Описание"] = df["Описание"].fillna("").apply(clean_text)
df["Ключевые слова"] = df["Ключевые слова"].fillna("").apply(clean_text)

# Функция для расчета коэффициента Жаккара
def calculate_jaccard(description, keywords):
    # Разделение текста на уникальные слова
    desc_set = set(description.split())
    keywords_set = set(keywords.split())
    
    # Если оба набора пусты, возвращаем 0 (никакой корреляции)
    if not desc_set and not keywords_set:
        return 0
    
    # Вычисление коэффициента Жаккара
    intersection = len(desc_set.intersection(keywords_set))
    union = len(desc_set.union(keywords_set))
    return intersection / union

# Создание нового столбца "Корреляция" на основе коэффициента Жаккара
df["Корреляция"] = df.apply(lambda row: calculate_jaccard(row["Описание"], row["Ключевые слова"]), axis=1)

# Просмотр первых 5 строк с новым столбцом "Корреляция"
print(df.head())

# Сохранение обновленного датасета в новый CSV файл (если необходимо)
cleaned_file_path = 'cleaned_data_with_correlation.xlsx'
df.to_excel(cleaned_file_path, index=False)

# Фильтрация строк, где значение "Корреляция" больше 0
df_filtered = df[df["Корреляция"] > 0]
df_filtered = df_filtered.sort_values(by="Корреляция", ascending=False)

# Сохранение отфильтрованного датасета в новый CSV файл
filtered_file_path = 'filtered_data.xlsx'
df_filtered.to_excel(filtered_file_path, index=False)
print(f"\nФайл с отфильтрованными данными сохранен по адресу: {filtered_file_path}")

# Печать первых 5 строк отфильтрованного датасета
print(df_filtered.head())

print(f"\nОбработанный файл сохранен по адресу: {cleaned_file_path}")
