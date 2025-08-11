import pandas as pd
import matplotlib.pyplot as plt

# 1. Читаємо файл прямо з Google Sheets
url = "https://docs.google.com/spreadsheets/d/1bclX5PbqE8zR1-wOSM3ZTFa53sIC7RXqwty7Abmw9yQ/export?format=csv&id=1bclX5PbqE8zR1-wOSM3ZTFa53sIC7RXqwty7Abmw9yQ&gid=1724592523"
df = pd.read_csv(url)

# 2. Перегляд перших рядків
print(df.head())

# 3. Розмір таблиці
print("Shape:", df.shape)

# 4. Типи даних
print(df.dtypes)

# 5. Частка пропусків у кожній колонці
print(df.isnull().sum() / len(df))

# 6. Видалення всіх колонок з пропусками, крім "Мова програмування"
cols_to_keep = ["Мова програмування"]
df_clean = df[cols_to_keep + [col for col in df.columns if col not in cols_to_keep and df[col].isnull().sum() == 0]]

# 7. Перевірка пропусків
print(df_clean.isnull().sum() / len(df_clean))

# 8. Знаходимо колонку із зарплатою автоматично
salary_col = [col for col in df.columns if "Зарплата" in col][0]
print("Колонка із зарплатою:", salary_col)

# 9. Залишаємо тільки рядки з Python та заповненою зарплатою і посадою
df_no_na = df.dropna(subset=["Мова програмування", "Посада", salary_col])
python_data = df_no_na[df_no_na["Мова програмування"] == "Python"]

print("Python shape:", python_data.shape)

# 10. Якщо дані є, будуємо статистику
if not python_data.empty:
    grouped = python_data.groupby("Посада")

    salary_stats = grouped.agg({salary_col: ["min", "max"]})
    salary_stats.columns = ["min_salary", "max_salary"]

    # середнє
    salary_stats["avg"] = (salary_stats["min_salary"] + salary_stats["max_salary"]) / 2

    # описова статистика
    print(salary_stats["avg"].describe())

    # збереження CSV
    salary_stats.to_csv("salary_stats.csv", index=True)
    print("Готово! Файл salary_stats.csv збережено.")

    # --- ГРАФІКИ ---
    plt.figure(figsize=(10, 6))
    salary_stats[["min_salary", "max_salary"]].plot(kind="bar", figsize=(10, 6))
    plt.title("Мінімальна та максимальна зарплата (Python) за посадою")
    plt.ylabel("Зарплата")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    salary_stats["avg"].sort_values().plot(kind="barh", figsize=(10, 6), color="skyblue", edgecolor="black")
    plt.title("Середня зарплата (Python) за посадою")
    plt.xlabel("Середня зарплата")
    plt.ylabel("Посада")
    plt.tight_layout()
    plt.show()
else:
    print("⚠ Немає даних для мови Python — графіки не побудовані.")
