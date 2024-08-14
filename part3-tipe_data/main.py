# tipe data: Angka (integer dan float)
data_integer = 10
print("data : ", data_integer, ", bertipe : ", type(data_integer), "\n")

data_float = 10.5
print("data : ", data_float, ", bertipe : ", type(data_float), "\n")

# tipe data: Karakter (String)
data_string = "ucup"
print("data : ", data_string, ", bertipe : ", type(data_string), "\n")

# tipe data: Biner (boolean)
data_bool = True
print("data : ", data_bool, ", bertipe : ", type(data_bool), "\n")


# tipe data khusus

# bilangan kompleks
data_complex = complex(5, 6)
print("data : ", data_complex, ", bertipe : ", type(data_complex), "\n")

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)
print("data : ", data_c_double, ", bertipe : ", type(data_c_double), "\n")
