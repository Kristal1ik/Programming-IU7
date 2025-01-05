import numpy as np


a = np.arange(12)
print('Массив ', a, '\n')

b = np.reshape(a, (2, 6))
print('Изменение форм массива\n', b, '\n')

c = np.resize(a, (2, 7))
print("Изменение форм массива при несовпадении числа элементов\n", c, "\n")
