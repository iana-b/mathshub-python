import numpy as np
# 1
# 1 способ
# arr = np.array([[True, True, True], [True, True, True], [True, True, True]])
# print(arr)

# 2 способ
# s = (3, 3)
# arr_2 = np.ones(s, dtype=bool)
# print(arr_2)

# 3 способ
# arr_3 = np.full((3, 3), True)
# print(arr_3)

# 2
# a = arr[arr > 0]
# print(a)
# a = np.array([[1, 3, 5], [1, 2, 3]])
# a[a % 2 != 0] = -1
# print(a)

# arr = np.array([[1, 3, 5], [1, 2, 3]])
# print(arr)
# arr[(arr > 0) & (arr % 2 != 0)] = -1
# print(arr)

# 3
# a = np.array([[1, 3, 5], [1, 2, 3]])
# b = np.array([[1, 3, 7], [9, 2, 9]])
# c = np.intersect1d(a, b)
# print(c)

# 4
# a = np.array([[1, 2, 5], [1, 2, 1], [1, 2, 2]])
# print(a)
# a[:, [0, 1]] = a[:, [1, 0]]
# print(a)

# 5
# a = np.array([-1, -5, 2, 5, 10, 256, 280, -5])
# a[a < 0] = 0
# a[a > 255] = 255
# print(a)
#
# a = np.array([-1, -5, 2, 5, 10, 256, 280, -5])
# print(a)
# print(a.clip(0, 255))

# 6
# arr = np.random.randint(-100, 100, (3, 3))
# print(arr)
# print(arr.ravel())

# 7
# arr = np.random.randint(-100, 100, (2, 3))
# print(arr)
# print(arr.max(axis = 1))

# 8
# arr = np.array([1, 2, 3, np.nan, 4, 5, np.nan, 6, 7, np.nan, 8 ])
# print(arr)
# print(arr[~ np.isnan(arr)])

# 9


# import numpy as np
# import pandas as pd
# # import scipy.stats as sps
#
# # import warnings
# # warnings.simplefilter('ignore', FutureWarning)
#
# data = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", header=None, sep=",")
# data.columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
#                 "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week",
#                 "native-country", "salary"]
# data.sex = data.sex.apply(lambda x: x.strip())
# data['native-country'] = data['native-country'].apply(lambda x: x.strip())
# data.head()
#
# # 1
# # c = data.groupby('sex').agg({'race': 'count'})
# # print(c)
#
# # 2
# # age = data[data['sex'] == 'Female'].age.mean()
# # print(age)
#
# # 3
# # n = (data[data['native-country'] == 'Germany'].shape[0] / data['native-country'].shape[0]) * 100
# # print(n)
#
# # 4-5
# data.query('fnlwgt < 50000')


# print(f'Больше: {round(data[data["salary"]==">50K"]["age"].mean(),0)} +- {round(data[data["salary"]==">50K"]["age"].std(),1)}')
# print(f'Меньше: {round(data[data["salary"]=="<=50K"]["age"].mean(),0)} +- {round(data[data["salary"]=="<=50K"]["age"].std(),1)}')



# a = np.linspace(0, 8, 7)
# print(a)

# arr = np.linspace(10, 20, 21)
# print(arr)

# a = np.linspace(0, 10, 5)
# print(a, a[0])
# b = np.array([1, 2, 6])
# print(b)
# a[0] = 1
# print(a)
# a = a.astype(str)
# a[0] = 'hello'
# print(a)
# c = np.concatenate([a, b])
# print(c)
# cc = np.concatenate([b, a])
# print(cc)

# bb = np.linspace(0, 1, 5)
# print(bb)
# b = np.logspace(0, 1, 5)
# print(b)

# mixed_array = np.array([1, 2, 3, 'H'])
# print(mixed_array)
# mixed_array[0] = 'Hello world, this is a test'
# print(mixed_array)

# a = np.array([1, 2, 3, 5.])
# print(a)
