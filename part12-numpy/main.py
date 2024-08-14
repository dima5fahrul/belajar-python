import numpy as np

# Create a 1D array
a = np.array([1, 2, 3, 4, 5])
print(a)

# Create a 2D array
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

# Create a 3D array
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(c)

# Create an array of zeros
d = np.zeros((2, 3))
print(d)

# Create an array of ones
e = np.ones((2, 3))
print(e)


# membuat vector dengan range
f = np.arange(10)
print(f)

# membuat linear space
g = np.linspace(1, 10, 5)
print(g)

print("====================")

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Penjumlahan
c = a + b
print(c)

# Pengurangan
d = a - b
print(d)

# Perkalian
e = a * b
print(e)

# Pembagian
f = a / b
print(f)

# Perpangkatan
g = a**b
print(g)

print("======================")

a = np.arange(10) ** 2
print(a)

# Mengambil nilai berdasarkan index
print(a[2])
print(a[2:5])
print(a[:5])
print(a[5:])

print("======================")

a = np.array(([1, 2], [5, 6]))
b = np.ones((2, 2))
print(a)
print(b)

# perkalian matrix
c = np.dot(a, b)
d = a.dot(b)
print(c)
print(d)
