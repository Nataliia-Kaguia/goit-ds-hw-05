import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub

# Завантаження датасету з Kaggle
path = kagglehub.dataset_download("sootersaalu/amazon-top-50-bestselling-books-2009-2019")
df = pd.read_csv(f"{path}/bestsellers with categories.csv")

# Оновлення назв колонок
df.columns = ['name', 'author', 'user_rating', 'reviews', 'price', 'year', 'genre']

# 1. Перевірка пропусків
print(df.isna().sum())

# 2. Унікальні жанри
print(df['genre'].unique())

# 3. Розподіл цін
plt.figure(figsize=(8, 5))
sns.histplot(df['price'], bins=20, color='skyblue')
plt.title("Розподіл цін книг")
plt.show()

# Статистика по цінах
print("Максимальна ціна:", df['price'].max())
print("Мінімальна ціна:", df['price'].min())
print("Середня ціна:", df['price'].mean())
print("Медіанна ціна:", df['price'].median())

# Пошук і сортування
max_rating = df['user_rating'].max()
print("Найвищий рейтинг:", max_rating)
print("Кількість книг з таким рейтингом:", (df['user_rating'] == max_rating).sum())

max_reviews_book = df.loc[df['reviews'].idxmax()]
print("Книга з найбільшою кількістю відгуків:", max_reviews_book['name'])

# Найдорожчі книги 2015 року
plt.figure(figsize=(14, 10))
sns.barplot(
    data=books_2015.sort_values("price", ascending=False),
    x="price", y="name", hue="name", palette="viridis", legend=False
)
plt.title("Найдорожчі книги 2015 року", fontsize=16)
plt.xlabel("Ціна", fontsize=12)
plt.ylabel("Назва книги", fontsize=12)
plt.yticks(fontsize=9)  # зменшення шрифту для підписів
plt.xticks(fontsize=10)
plt.tight_layout()
plt.show()

# Fiction 2010 року
fiction_2010 = df[(df['genre'] == 'Fiction') & (df['year'] == 2010)]
print("Кількість Fiction 2010:", fiction_2010.shape[0])

# Рейтинг 4.9 у 2010 та 2011
rating_49 = df[(df['user_rating'] == 4.9) & (df['year'].isin([2010, 2011]))]
print("Кількість книг з рейтингом 4.9 у 2010-2011:", rating_49.shape[0])

# Сортування 2015 року < 8$
cheap_books_2015 = books_2015[books_2015['price'] < 8].sort_values("price")
print("Остання книга у списку дешевих 2015:", cheap_books_2015.iloc[-1]['name'])

# Агрегування
agg_prices = df.groupby('genre')['price'].agg(['max', 'min'])
print(agg_prices)

# Кількість книг на автора
author_books = df.groupby('author')['name'].count().reset_index(name='book_count')
print("Розмірність:", author_books.shape)
top_author = author_books.loc[author_books['book_count'].idxmax()]
print("Автор з найбільшою кількістю книг:", top_author['author'], "-", top_author['book_count'])

# Середній рейтинг на автора
author_rating = df.groupby('author')['user_rating'].mean().reset_index(name='avg_rating')
min_rating_author = author_rating.loc[author_rating['avg_rating'].idxmin()]
print("Мінімальний середній рейтинг у:", min_rating_author['author'], "-", min_rating_author['avg_rating'])

# Топ-10 авторів за кількістю книг
top_authors = merged_df.sort_values("book_count", ascending=False).head(10)

plt.figure(figsize=(12, 8))
sns.barplot(
    data=top_authors.reset_index(),
    x="book_count", 
    y="author", 
    hue="author", 
    dodge=False, 
    palette="coolwarm",
    legend=False
)
plt.title("Топ-10 авторів за кількістю книг у рейтингу Топ-50", fontsize=16)
plt.xlabel("Кількість книг", fontsize=12)
plt.ylabel("Автор", fontsize=12)
plt.yticks(fontsize=10)
plt.xticks(fontsize=10)
plt.tight_layout()
plt.show()

