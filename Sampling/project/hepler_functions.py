# импортируем библиотеки
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

# создаем функцию которая будет возвращать статистические значение которое требуется по его названию
def choose_statistic(x, sample_stat_text):
  # для расчета среднего значения sample_stat_text должен быть равен слову Mean
  if sample_stat_text == "Mean":
    return np.mean(x)
  elif sample_stat_text == "Minimum":
    return np.min(x)
  elif sample_stat_text == "Variance":
    return np.var(x, ddof=1)
  # вы можете добавить свои значения
  else:
    raise Exception('Make sure to input "Mean", "Minimum", or "Variance"')

# создаем отдельный метод который поможет посмотрить гистограмму
def population_distribution(population_data):
  sns.histplot(population_data, stat='density')
  plt.title(f"Population Distribution")
  plt.xlabel('')
  plt.show()
  plt.clf()

# создаем отдельный метод который соберет для нас список статистических значений выборок и сразу строит его график
def sampling_distribution(population_data, samp_size, stat):
  sample_stats = []
  for i in range(500):
    samp = np.random.choice(population_data, samp_size, replace = False)
    sample_stat = choose_statistic(samp, stat)
    sample_stats.append(sample_stat)
  
  pop_statistic = round(choose_statistic(population_data, stat),2)
  sns.histplot(sample_stats, stat='density')
  plt.title(f"Sampling Distribution of the {stat} \nMean of the Sample {stat}s: {round(np.mean(sample_stats), 2)} \n Population {stat}: {pop_statistic}")
  plt.axvline(pop_statistic,color='g',linestyle='dashed', label=f'Population {stat}')
  plt.axvline(np.mean(sample_stats),color='orange',linestyle='dashed', label=f'Mean of the Sample {stat}s')
  plt.legend()
  plt.show()
  plt.clf()