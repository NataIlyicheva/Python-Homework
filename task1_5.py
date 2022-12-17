# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в
# 2D пространстве. Формула вычисления расстояния между двумя точками A(xa, ya) и B(xb, yb) на плоскости: 
# AB = √(xb - xa)2 + (yb - ya)2"

x_a = int(input())
y_a = int(input())
x_b = int(input())
y_b = int(input())
import math
number = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
print(round(math.sqrt(number), 3))