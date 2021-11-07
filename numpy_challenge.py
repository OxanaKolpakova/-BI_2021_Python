# Создайте 3 ваших любимых эррея разными способами
# Создайте функцию matrix_multiplication, которая принимает 2 матрицы, перемножает их по соответствующим правилам и выдаёт получившуюся матрицу
def matrix_multiplication(arr1, arr2):
	import numpy as np
	arr3 = np.dot(arr1, arr2)
	return(arr3)


# Создайте функцию multiplication_check, которая принимает список с матрицами, и выдаёт True, если они могут быть перемножены друг на друга в порядке, в котором они находятся в списке, и False, если их нельзя перемножить
def multiplication_check(arrlist):
  for i in range(len(arrlist)-1):
    if arrlist[i].shape[1] == arrlist[i+1].shape[0]:
      check = "TRUE"
    else:
      check = "FALSE"
      return(check)
  return(check)


# Создайте функцию multiply_matrices, которая принимает список с матрицами, и выдаёт результат перемножения, если его можно получить, или возвращает None, если их нельзя перемножить
def multiply_matrices(arrlist):
  if multiplication_check(arrlist) == "TRUE":
    res = arrlist[0]
    for i in arrlist[1:]:
      res = np.dot(res, i)
    return res
  else:
    return "NONE"


# Создайте функцию compute_2d_distance, принимающую 2 одномерных эррея c парой значений (как координаты точки на плоскости) и вычисляющую расстояние между ними
def compute_2d_distance(arr1, arr2):
  import scipy
  import scipy.spatial
  Z = np.vstack((arr1, arr2))
  D = scipy.spatial.distance.cdist(Z,Z)
  return D[1][0]


# Создайте функцию compute_multidimensional_distance, принимающую 2 одномерных эррея с любым количеством значений (но равным) и вычисляющую расстояние между ними
def compute_multidimensional_distance(arr10, arr20):
  from scipy.spatial import distance
  D = distance.euclidean(arr10, arr20)
  return D

# Создайте функцию compute_pair_distances, которая получает 2d эррей, где каждая строка это наблюдение, а каждый столбец - фича. Функция рассчитывает матрицу попарных расстояний и выдаёт её пользователю
def compute_pair_distances(arr):
  import scipy
  import scipy.spatial
  D = scipy.spatial.distance.cdist(arr,arr)
  return D


if __name__ == '__main__':
  import numpy as np
  arr1 = np.ones((10,20))
  arr2 = np.zeros((10,10))
  arr3 = np.random.random((10,10))
  arrlist1 = [arr1, arr2, arr3]
  arrlist2 = [arr2, arr2, arr3]
  arr10 = [1,0]
  arr20 = [2,2]
  arr30 = [1,0,0]
  arr40 = [2,2,0]
  print(matrix_multiplication(arr3, arr2))
  print(multiplication_check(arrlist1))
  print(multiply_matrices(arrlist2))
  print(compute_2d_distance(arr10, arr20))
  print(compute_multidimensional_distance(arr30, arr40))
  print(compute_pair_distances(arr3))
  