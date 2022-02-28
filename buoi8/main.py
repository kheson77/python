# #1
import numpy as np
# print(np.__version__)

# #2
vector2 = np.arange(10, 50)

# #3
vector3 = np.arange(10, 50)
print(vector3.size)

# #4
vector4 = np.arange(10, 50)
reverse_vector = vector4[::-1]

# #5
vector5 = np.arange(10,18).reshape(2, 2, 2)

# #6
vector_6 = np.array([1, 2, 0, 0, 4, 0])
print(f"Lấy ra các phần tử có giá trị khác 0:\n{vector_6[vector_6 != 0]}")

# a = [[1,2,3],[4,5,6]]

# for x in a:
#     print(x)
#     for index, value in enumerate(x):
#         x[index] +=  2

# print(a)

# a = np.array([[1,2,3],[4,5,6]])
# a + 2
# print(a)

# #7
matrix_7 = np.random.random((10,30))
print(f"Tạo một matrix 10x30 với các giá trị ngẫu nhiên:\n{matrix_7}")
print(f"Max: {np.max(matrix_7)}")
print(f"Min: {np.min(matrix_7)}")

# #8
vetor_8 = np.random.random(30)
print(f"Tạo vector có kích thước 30 phần tử giá trị ngẫu nhiên:\n{vetor_8}\nSize: {vetor_8.size}")
print(f"Avg: {np.mean(vetor_8)}")

# #9
matrix_9 = np.full((5,5), 0)
matrix_9[0] = 1
matrix_9[-1] = 1
matrix_9[:, 0] = 1
matrix_9[:, -1] = 1
print(f"Tạo matrix hình vuông (số hàng = số cột) với các giá trị 1 ở viền và 0 ở giữa:\n{matrix_9}")

# #10
ndarray_10 = np.random.randint(1000, size=(6, 7, 8))
vector_10 = ndarray_10.flatten()
print(f"Tạo một ndarray có shape = (6, 7, 8) với các giá trị số nguyên bất kỳ, in ra giá trị của phần tử thứ 100:\n{vector_10[99]}")