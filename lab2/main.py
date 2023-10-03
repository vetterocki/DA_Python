import numpy as np
import pandas as pd
from scipy import stats
from dict_utils import joined


def find_mean(columns, csv_data):
    return list(map(lambda column: np.mean(csv_data[column]), columns))


def check_if_normal(columns, csv_data):
    return list(map(lambda column: stats.normaltest(csv_data[column]).pvalue, columns))


def check_if_crime_rate_increased(columns, csv_data):
    return stats.ttest_rel(*[csv_data[column] for column in columns], alternative='less').pvalue


def calculate_correlation(columns, csv_data):
    result = {}
    confidence_level = 0.05
    for i in range(0, len(columns), 2):
        first, second = columns[i], columns[i + 1]
        is_normal = any(p < confidence_level for p in check_if_normal([first, second], csv_data))
        correlation_func = stats.spearmanr if is_normal else stats.pearsonr
        result[correlation_func(csv_data[first], csv_data[second])] = "Spearman" if is_normal else "Pearson"
    return result


data = pd.read_csv("lab2\Crime.csv")
crime_rates_columns = ["CrimeRate", "CrimeRate10"]

print(f"""
1.Знайти середню частоту злочинів (зараз і десять років тому): 
{find_mean(crime_rates_columns, data)}
2.Перевірити чи нормально розподілена частота злочинів (зараз і десять років тому):
p_values, {check_if_normal(crime_rates_columns, data)}
3.Перевірити за допомогою статистичних гіпотез чи зросла частота злочинів за 10 років:
p_value, {check_if_crime_rate_increased(crime_rates_columns, data)}
4.Який зв’язок між частотою злочинів і витратами на поліцію (коефіцієнт Спірмена): \n
{joined(calculate_correlation(["CrimeRate", "ExpenditureYear0", "CrimeRate10", "ExpenditureYear10"], data))}
""")
