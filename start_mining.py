# Импорт необходимых библиотек
import pandas as pd
import numpy as np

# Чтение .csv файла
file_path = 'path_to_your_file.csv'  # Замените на путь к вашему файлу
df = pd.read_csv(file_path)

# Просмотр первых строк данных
print("Первые 5 строк данных:")
display(df.head())

# Информация о структуре данных
print("\nИнформация о датасете:")
df.info()

# Описание числовых признаков
print("\nСтатистическое описание числовых признаков:")
display(df.describe())

# Поиск пропущенных значений
print("\nКоличество пропущенных значений в каждом столбце:")
display(df.isnull().sum())

# Удаление дублирующихся строк
df = df.drop_duplicates()
print("\nКоличество строк после удаления дубликатов:", len(df))

# Заполнение пропущенных значений
# Заполнение числовых признаков средним значением
df = df.fillna(df.mean())

# Заполнение категориальных признаков наиболее частым значением
df = df.apply(lambda x: x.fillna(x.mode()[0]) if x.dtype == 'object' else x)

print("\nКоличество пропущенных значений после заполнения:")
display(df.isnull().sum())

# Преобразование категориальных переменных в числовые (если необходимо)
df = pd.get_dummies(df)

# Нормализация числовых признаков (мин-макс)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df[df.columns] = scaler.fit_transform(df[df.columns])

print("\nПервые 5 строк данных после нормализации:")
display(df.head())

# Сохранение очищенного и обработанного датасета в новый файл
cleaned_file_path = 'cleaned_data.csv'
df.to_csv(cleaned_file_path, index=False)
print(f"\nОбработанный файл сохранен по адресу: {cleaned_file_path}")
