import numpy as np
import dict_utils as du
import pandas as pd


def generate_arrays():
    default_array = np.array([[12, 14, 19, 20], [13, 15, 16, 21], [14, 22, 17, 19]], dtype=float)
    arranged_array = np.arange(10, 20, 2)
    ones_array = np.ones((5, 4), dtype=int)
    zeros_array = np.zeros((5, 4), dtype=int)
    linspaced_array = np.linspace(1, 10, 4)
    random_array = np.random.random((5, 4))
    random_integers_array = np.random.randint(0, 100, (4, 4))
    empty_array = np.empty(5)
    return du.create(locals())


arrays = generate_arrays()

print(du.joined(arrays))


def access_array_elements(od_array, tw_array):
    positive_index = od_array[1]
    negative_index = od_array[-1]
    two_dimensional_index = tw_array[-1, 2]
    one_dimensional_slice = od_array[2:4]
    two_dimensional_slice = tw_array[0:2, 1:3]
    return du.create(locals())


samples = arrays["Arranged_array"], arrays["Default_array"]
accesses = access_array_elements(*samples)

print(du.joined(accesses))


def perform_array_operations(od_array, tw_array):
    reduced_by_add = np.add.reduce(od_array)
    accumulated_by_multiply = np.multiply.accumulate(od_array)
    outer_by_divide = np.divide.outer(od_array, [1, 2, 3])
    subtract = np.subtract(tw_array, [1, 2, 3, 4])
    power = np.power(od_array, 2)
    negative = np.negative(tw_array)
    return du.create(locals())


operations = perform_array_operations(*samples)
print(du.joined(operations))

data = pd.read_csv('iris.csv')
petal = np.array(data['petal_width'])


def calculate(data_array):
    min_value = np.min(data_array)
    max_value = np.max(data_array)
    mean = np.mean(data_array)
    var = np.var(data_array)
    std = np.std(data_array)
    median = np.median(data_array)
    percentiles = np.percentile(data_array, 25), np.percentile(data_array, 75)
    return du.create(locals())


statistics = calculate(petal)
print(du.joined(statistics))
