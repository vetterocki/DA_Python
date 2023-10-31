import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('penguins.csv')


def first():
    species_counts = data.groupby('species').count()
    species_counts.plot(kind='bar', title='Кількість пінгвінів кожного виду')
    plt.show()
    min_culmen_length = data.groupby('species')['culmen_length_mm'].min()
    min_culmen_length.plot(kind='bar', title='Мінімальна довжина дзьобу кожного виду')
    plt.show()
    avg_weight_by_species_sex = data.groupby(['species', 'sex'])['body_mass_g'].mean()
    avg_weight_by_species_sex.unstack().plot(kind='bar', title='Середня вага пінгвінів за видом та статтю')
    plt.show()


first()


def second():
    data['culmen_depth_mm'].plot.hist(bins=20, title='Гістограма глибини дзьобу')
    plt.show()
    for species in data['species'].unique():
        species_data = data[data['species'] == species]
        species_data['culmen_depth_mm'].plot.hist(bins=20, title=f'Гістограма глибини дзьобу ({species})')
        plt.show()


second()


def third():
    data.boxplot(column='flipper_length_mm')
    plt.title('Діаграма розмаху довжини ласт (загальна)')
    plt.show()
    data.boxplot(column='flipper_length_mm', by='species')
    plt.title('Діаграма розмаху довжини ласт (за видами)')
    plt.show()


third()


def fourth():
    data.plot.scatter(x='culmen_length_mm', y='culmen_depth_mm')
    plt.title('Діаграма розсіювання для довжини і глибини дзьобу')
    plt.show()
    correlation_culmen = data['culmen_length_mm'].corr(data['culmen_depth_mm'])
    print(f'Коефіцієнт кореляції для довжини і глибини дзьобу: {correlation_culmen}')
    data.plot.scatter(x='body_mass_g', y='flipper_length_mm')
    plt.title('Діаграма розсіювання для ваги і довжини ласт')
    plt.show()
    correlation_weight_flipper = data['body_mass_g'].corr(data['flipper_length_mm'])
    print(f'Коефіцієнт кореляції для ваги і довжини ласт: {correlation_weight_flipper}')


fourth()
