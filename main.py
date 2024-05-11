import numpy as np

list = [1, -2, 3, 0, -5, 6]
arr = np.array(list) # переводим список в numpy массив

zeros = np.zeros(10)
ones = np.ones(10)
nums = np.full(20, 123)
zeros[0] = 123
print(zeros)

nums1 = np.arange(100, 201)
print(nums1)
