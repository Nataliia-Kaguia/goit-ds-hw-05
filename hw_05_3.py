import kagglehub
import pandas as pd
import os
import matplotlib.pyplot as plt

# 1. Завантаження датасету з Kaggle
print("Завантаження датасету...")
dataset_path = kagglehub.dataset_download(
    "sootersaalu/amazon-top-50-bestselling-books-2009-2019"
)

# 2. Формування повного шляху до файлу
file_path = os.path.join(dataset_path, "bestsellers with categories.csv")

if not os.path.exists(file_path):
    raise FileNotFoundError(f"Файл не знайдено: {file_path}")

# 3. Читання CSV
df = pd.read_csv(file_path)
print("\nПерші 5 рядків датасету:")
print(df.head())

# 4. Загальна інформація
print("\nІнформація про датафрейм:")
print(df.info())

# 5. Мін/макс ціни
print("\nМінімальна ціна:", df["Price"].min())
print("Максимальна ціна:", df["Price"].max())

# 6. Мін/макс відгуків
print("\nМінімальна кількість відгуків:", df["Reviews"].min())
print("Максимальна кількість відгуків:", df["Reviews"].max())

# 7. Середній рейтинг по категоріях
avg_rating = df.groupby("Genre")["User Rating"].mean()
print("\nСередній рейтинг по категоріях:")
print(avg_rating)

# 8. Книги з рейтингом 5.0
best_books = df[df["User Rating"] == 5.0]
print("\nКниги з ідеальним рейтингом 5.0:")
print(best_books[["Name", "Author", "Year", "Price"]])

# 9. Топ-5 авторів за кількістю книг
top_authors = df["Author"].value_counts().head(5)
print("\nТоп-5 авторів за кількістю книг:")
print(top_authors)

# 10. Книги дорожчі за 30
expensive_books = df[df["Price"] > 30]
print("\nКниги дорожчі за $30:")
print(expensive_books[["Name", "Author", "Price"]])

# ==== ГРАФІКИ ====

# Графік 1: Розподіл цін
plt.figure(figsize=(8,5))
df["Price"].hist(bins=20, color="skyblue", edgecolor="black")
plt.title("Розподіл цін книг")
plt.xlabel("Ціна")
plt.ylabel("Кількість")
plt.grid(axis='y', alpha=0.75)
plt.show()

# Графік 2: Розподіл користувацьких рейтингів
plt.figure(figsize=(8,5))
df["User Rating"].hist(bins=10, color="lightgreen", edgecolor="black")
plt.title("Розподіл рейтингів")
plt.xlabel("Рейтинг")
plt.ylabel("Кількість книг")
plt.grid(axis='y', alpha=0.75)
plt.show()

# Графік 3: Середня ціна по жанрах
avg_price_by_genre = df.groupby("Genre")["Price"].mean()
avg_price_by_genre.plot(kind="bar", color=["orange", "purple"], figsize=(6,4))
plt.title("Середня ціна по жанрах")
plt.ylabel("Середня ціна")
plt.show()

# Графік 4: Кількість книг по роках
df["Year"].value_counts().sort_index().plot(kind="bar", figsize=(10,5), color="teal")
plt.title("Кількість книг по роках")
plt.xlabel("Рік")
plt.ylabel("Кількість книг")
plt.show()

# Графік 5: Топ-10 авторів
df["Author"].value_counts().head(10).plot(kind="barh", figsize=(8,6), color="coral")
plt.title("Топ-10 авторів за кількістю книг")
plt.xlabel("Кількість книг")
plt.gca().invert_yaxis()
plt.show()
