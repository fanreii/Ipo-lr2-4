import math
x = float(input("Введите значение x: "))
y = float(input("Ввдите значение y: "))
z = float(input("Введите значение z: "))
m = float
k = float
w = float 
w = (math.pow(math.fabs(math.cos(x) - math.sin(y)), 1+2*(math.pow(math.sin(y), 2)))) * (1 + z + ((math.pow(z, 2)) / 2) + (math.pow(z,3) / 3) + (math.pow(z, 4) / 4))
print("Функция w при данных значениях x, y, z принимает значение: ", w)