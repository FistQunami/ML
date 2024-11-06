import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

results = {
    '0000': [3, 5, 4, 6, 7, 5, 3, 4, 6, 5],
    '0001': [6, 7, 5, 5, 6, 8, 6, 5, 6, 7],
    '0010': [2, 4, 3, 2, 4, 3, 4, 2, 3, 4],
    '0011': [8, 7, 6, 7, 8, 7, 7, 8, 6, 7],
    '0100': [5, 6, 4, 5, 4, 5, 5, 6, 5, 4],
    '0101': [7, 6, 8, 7, 6, 8, 7, 6, 7, 6],
    '0110': [4, 3, 4, 3, 4, 5, 4, 3, 5, 4],
    '0111': [9, 8, 9, 7, 8, 9, 8, 9, 8, 7],
}

# Рассчитываем средние значения для каждого набора данных
average_freq = {key: np.mean(values) for key, values in results.items()}

# Создание графиков
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10), tight_layout=True)

# Гистограмма частот
sns.histplot(sum(results.values(), []), bins=16, kde=False, ax=ax1, color='skyblue')
ax1.set_title("Распределение частот результатов")
ax1.set_xlabel("Результаты измерений")
ax1.set_ylabel("Частота")

# Столбчатая диаграмма со средними значениями
sns.barplot(x=list(average_freq.keys()), y=list(average_freq.values()), ax=ax2, palette="viridis")
ax2.set_title("Средняя частота результатов по экспериментам")
ax2.set_xlabel("Результаты измерений")
ax2.set_ylabel("Средняя частота")

plt.show()
