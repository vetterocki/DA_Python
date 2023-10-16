import datetime as dt
import pandas as pd


def dataframe_copy(dataframe: pd.DataFrame) -> pd.DataFrame:
    subset = dataframe.iloc[:5, :3]
    subset.index = ['A', 'B', 'C', 'D', 'E']
    subset.columns = ['X', 'Y', 'Z']
    subset.loc["F"] = ["A Class", 2018, 83483]
    return subset


def process_dataframe(dataframe: pd.DataFrame):
    min_by_year = dataframe.groupby("year")["price"].min()
    print(min_by_year)

    current_year = dt.date.today().year
    filtered_cars = dataframe[
        (dataframe['transmission'] == 'Semi-Auto') &
        (current_year - dataframe['year'] <= 5) &
        (dataframe['mileage'] > 20000)
        ]
    print(filtered_cars)

    dataframe["total_fuel_consumed"] = dataframe["mpg"] * dataframe["mileage"]
    dataframe["average_volume"] = dataframe.groupby("model")["engineSize"].transform("mean")
    print(dataframe)


data = pd.read_csv("lab3\merc.csv")
result = dataframe_copy(data)
print("""
2. За допомогою зрізів зробити копію частини набору даних і зберегти до нового об’єкту DataFrame. 
Призначити йому власні індекси рядків та стовпців. Додати новий рядок. 
""", result)

print("""
3. Використовуючи початковий DataFrame:
а) Знайти мінімальну ціну для автомобілів кожного року реєстрації;
б) Вивести машини не старіші п’яти років з напівавтоматичною коробкою передач, що мають пробіг більше 20 тис миль.
в) Додати новий стовпець, який містить скільки всього палива витратив даний автомобіль за свою історію.
г) Додати новий стовпець, який містить середній об’єм двигуна для даної моделі.
""")
process_dataframe(data)
