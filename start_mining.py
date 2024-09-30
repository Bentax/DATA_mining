# Импорт необходимых библиотек
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Чтение .csv файла
file_path = 'path_to_your_file.csv'  # Замените на путь к вашему файлу
df = pd.read_csv(file_path)

# Просмотр первых строк данных
print("Первые 5 строк данных:")
display(df.head())

# Информация о структуре данных
print("\nИнформация о датасете:")
df.info()

# Проверка наличия пропущенных значений
print("\nКоличество пропущенных значений в каждом столбце:")
display(df.isnull().sum())

# Удаление столбцов с высоким количеством пропусков
# Здесь я удаляю столбцы, где менее 30% значений не заполнены.
threshold = 0.3
df = df[df.columns[df.notnull().mean() > threshold]]
print("\nСтолбцы, оставленные после удаления с высоким уровнем пропусков:")
display(df.columns)

# Заполнение пропусков в числовых столбцах средним значением
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

# Заполнение пропусков в категориальных столбцах наиболее частым значением
categorical_cols = df.select_dtypes(include=['object']).columns
df[categorical_cols] = df[categorical_cols].apply(lambda x: x.fillna(x.mode()[0]) if not x.mode().empty else x)

# Преобразование категориальных переменных в числовые (one-hot encoding)
df = pd.get_dummies(df, drop_first=True)

# Нормализация числовых признаков (если числовые признаки есть)
if not df.empty and len(numeric_cols) > 0:
    scaler = MinMaxScaler()
    df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

print("\nПервые 5 строк данных после обработки:")
display(df.head())

# Сохранение очищенного и обработанного датасета в новый файл
cleaned_file_path = 'cleaned_data.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"\nОбработанный файл сохранен по адресу: {cleaned_file_path}")
