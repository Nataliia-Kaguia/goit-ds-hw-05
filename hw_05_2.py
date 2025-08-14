import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Прочитати файл з Google Sheets
url = "https://docs.google.com/spreadsheets/d/1bclX5PbqE8zR1-wOSM3ZTFa53sIC7RXqwty7Abmw9yQ/export?format=csv&gid=1724592523"
df = pd.read_csv(url)

# 2. Перші рядки
print(df.head())

# 3. Розмір таблиці
print("\nShape:", df.shape)

# 4. Типи даних
print("\nDtypes:\n", df.dtypes)

# 5. Частка пропусків у кожній колонці
print("\nMissing values (%):\n", df.isnull().sum() / len(df) * 100)

# 6. Видалити стовпці з пропусками, крім "Мова програмування"
cols_to_keep = ["Мова програмування"]
df_clean = df.dropna(axis=1, how='any').join(df[cols_to_keep])

# 7. Перевірка пропусків
print("\nMissing values after cleaning:\n", df_clean.isnull().sum() / len(df_clean) * 100)

# 8. Видалити рядки без пропусків у вихідній таблиці
df_dropna = df.dropna()

# 9. Новий розмір таблиці
print("\nShape after dropna:", df_dropna.shape)

# 10. Створити python_data
python_data = df[df["Мова програмування"] == "Python"]

# 11. Розмір python_data
print("\nPython data shape:", python_data.shape)

# 12. Групування за посадою
grouped = python_data.groupby("Посада")

# 13. Мін/макс зарплата по кожній посаді
agg_salary = grouped.agg(
    min_salary=("Зарплата на місяць", "min"),
    max_salary=("Зарплата на місяць", "max")
).reset_index()

print("\nMin/Max salary by position:\n", agg_salary)

plt.figure(figsize=(10, 6))
sns.barplot(
    data=agg_salary,
    x="Посада", y="max_salary",
    hue="Посада", palette="Blues", legend=False
)
sns.barplot(
    data=agg_salary,
    x="Посада", y="min_salary",
    hue="Посада", palette="Oranges", legend=False
)
plt.xticks(rotation=45)
plt.title("Мінімальна та максимальна зарплата по посадах (Python)")
plt.show()

# 14. Функція для середньої зарплати
def fill_avg_salary(row):
    return (row["min_salary"] + row["max_salary"]) / 2

agg_salary["avg"] = agg_salary.apply(fill_avg_salary, axis=1)

# 15. Описова статистика по "avg"
print("\nDescribe avg:\n", agg_salary["avg"].describe())

# 16. Збереження таблиці
agg_salary.to_csv("agg_salary.csv", index=False)

# Графік середня зарплата серед мов програмування
avg_salary_lang = df.groupby("Мова програмування")["Зарплата на місяць"].mean().reset_index()

plt.figure(figsize=(10,6))
sns.barplot(
    data=avg_salary_lang,
    x="Мова програмування", y="Зарплата на місяць",
    hue="Мова програмування", palette="viridis", legend=False
)
plt.xticks(rotation=45)
plt.title("Середня зарплата серед мов програмування")
plt.show()

# Графік використання Python у різних типах компаній
python_company = df[df["Мова програмування"] == "Python"]["Тип компанії"].value_counts().reset_index()
python_company.columns = ["Тип компанії", "Кількість"]

plt.figure(figsize=(8,5))
sns.barplot(
    data=python_company,
    x="Тип компанії", y="Кількість",
    hue="Тип компанії", palette="mako", legend=False
)
plt.xticks(rotation=45)
plt.title("Використання Python у різних типах компаній")
plt.show()
