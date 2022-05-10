import numpy as np

# v1 = np.array([1, 2, 3])
# v2 = np.array([[1, 2, 4], [5, 1, 2], [2, 1, 2]])
# v3 = np.array([[[1,2], [1,2]], [[3, 4], [5, 6]]])
# print(v3)
# print(v3.dtype)
# print(v3.shape)

# print(np.zeros(4))
# print(np.zeros((2, 3)))
# print(np.zeros(((3, 3, 3))))

# print(np.arange(0, 4))

# t = np.array([1, 2, 3, 4])
# print(t)
# print(t[3])
# print(t[:3])
# print(t[1:2])

# t2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(t2)
# print(t2[:,:2])

# t1 = np.array([[1, 2],[4, 5]])
# t2 = np.array([[7, 8],[0, 1]])
# print(t1.dot(t2))

# t1 = np.array([[1],[2]])
# print(t1)
# t2 = np.array([[3, 4]])
# print(t2)

# print(t2 * 2)

t2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print("max", t2.sum(axis=0))
# print("min", t2.sum(axis=1))
# print("sum ", t2.sum())
# print("평균", t2.mean())
# print("중간", np.median(t2))
print("최대 인덱스", t2.argmax())
print("최소 인덱스", t2.argmin())