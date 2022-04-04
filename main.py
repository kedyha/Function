# #lessons_1
# import random
# def mass_sum():
#     mass = [random.randint(0, 10) for i in range(10)]
#     print(mass)
#     return print(sum(mass))
# mass_sum()

#lessons_2

# def is_year_leap(year):
#     return year % 4 == 0 and  year % 100 != 0 or  year % 400 ==0
#
#
# while True:
#     print(is_year_leap(int(input("введите год: "))))

#lessons_3
# import math
#
# def square(side):
#     p = side *2
#     s = side ** 2
#     d = math.sqrt(2)*side
#
#     return f"пеприм = {p} , плос = {s}, диагональ = {d}"
# print(square(int(input("введите сторону квадрата: "))))