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

# def is_prime(numb):
#     k = 0
#     for i in range(2, numb // 2 + 1):
#         if (numb % i == 0):
#             k = k + 1
#     if (k <= 0):
#         print("Число простое")
#     else:
#         print("Число не является простым")
# print(is_prime(int(input())))


#home_work
#
# def calculater(a,b,c):
#     if c =='+':
#         print(a+b)
#     elif c =='-':
#         print(a-b)
#     while True:
#         if c == 0:
#             break
#
# print(calculater(int(input("чисо1")),int(input("число2")),input("введите операцию + - или 0 для выхода ")))
#
#
#_____________________________________________________________________________________
#FUNCTION_2

#task_1
#
#
# def razr(n):
#     s = 0
#     while n>0:
#         n=n//10
#         s+=1
#     return s
# print(razr(int(input())))

#task_2
# while True:
#     import math
#
#     def circle(r):
#         return math.pi*r**2
#
#     def rectangle(a,b):
#         return a*b
#
#     def triangle(a,b,c):
#         p = (a+b+c)/2
#         return math.sqrt(p*(p-a)*(p-b)*(p-c))
#
#     inuut = input("введите с для круга r для прямоугольника t для треугольника")
#
#     if inuut == 'c':
#         print(circle(int(input("введите радиус"))))
#     elif inuut == 'r':
#         print(rectangle(int(input("сторона 1 ")),int(input("сторона 2 "))))
#     elif inuut == 't':
#         print(triangle(int(input("сторона треугольника")),int(input("сторона треугольника")),
#                        int(input("сторона треугольника"))))


