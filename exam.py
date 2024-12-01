import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

results = {
'1100': [6, 4, 3, 6, 4, 3, 7, 8, 5, 3],
'0001': [6, 5, 7, 6, 6, 6, 4, 3, 7, 8],
'0110': [8, 6, 12, 4, 9, 5, 5, 6, 11, 4],
'1001': [6, 10, 4, 6, 7, 5, 7, 4, 4, 9],
'0101': [6, 12, 6, 4, 11, 6, 3, 5, 9, 10],
'0100': [8, 7, 3, 4, 4, 4, 7, 10, 6, 7],
'0111': [6, 7, 10, 10, 5, 10, 5, 5, 4, 6],
'1000': [8, 5, 7, 11, 3, 6, 8, 5, 7, 8],
'1101': [8, 7, 6, 7, 6, 4, 7, 8, 7, 9],
'1111': [7, 3, 6, 6, 5, 8, 6, 4, 1, 5],
'1010': [8, 3, 6, 7, 8, 9, 7, 5, 4, 9],
'1011': [8, 2, 8, 6, 6, 11, 6, 7, 11, 3],
'1110': [7, 10, 5, 4, 12, 6, 9, 5, 8, 5],
'0011': [2, 8, 9, 8, 5, 8, 8, 10, 9, 4],
'0000': [3, 5, 6, 6, 6, 5, 5, 6, 2, 6],
'0010': [3, 6, 2, 5, 3, 4, 6, 9, 5, 4],
}

# Рассчитываем средние значения для каждого набора данных
average_freq = {key: np.mean(values) for key, values in results.items()}

# Сортируем ключи для диаграммы, если порядок важен
sorted_keys = sorted(average_freq.keys())

# Создание графиков
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), tight_layout=True)

# Гистограмма частот
sns.histplot(sum(results.values(), []), bins=16, kde=False, ax=ax1, color='skyblue')
ax1.set_title("Распределение частот результатов")
ax1.set_xlabel("Результаты измерений")
ax1.set_ylabel("Частота")

# Столбчатая диаграмма со средними значениями
sns.barplot(x=sorted_keys, y=[average_freq[key] for key in sorted_keys], ax=ax2, palette="viridis")
ax2.set_title("Средняя частота результатов")
ax2.set_xlabel("Результаты измерений")
ax2.set_ylabel("Средняя частота")

plt.show()
