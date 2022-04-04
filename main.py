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

#lessons_4
# def season(month):
#     if month == 12 or month == 1 or month == 2:
#         print("зима")
#     elif month == 3 or month == 4 or month == 5:
#         print("весна")
#     elif month == 6 or month == 7 or month == 8:
#         print("лето")
#     else:
#         print("осень")
#
#
# while True:
#     season(int(input("введите номер месяца")))

#lessons_5

def is_prime(numb):
    k = 0
    for i in range(2, numb // 2 + 1):
        if (numb % i == 0):
            k = k + 1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")
print(is_prime(int(input())))