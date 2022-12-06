# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.

print ('Введите число от 1 до 7:')
a = int(input())

if a < 1 or a > 7:
    print ('Такого дня недели нет')
elif a == 6 or a == 7:
    print ('Это выходной!')
else:
    print('Это будний день')

# 2. Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# a = not (x or y or z)
# b = not x and not y and not z
# print (a == b)

# 3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

print ('Введите координаты точек x и y, причем они одновременно не могут быть равными 0')
print ('x:')
x = int(input())
print ('y:')
y = int(input())
if x == 0 and y == 0:
    print ('Поменяйте хотя бы одну из координат')
    print('x:')
    x = int(input())
    print('y:')
    y = int(input())
elif x == 0 and y != 0:
    print('Ось x')
elif y == 0 and x != 0:
    print('Ось y')
elif x < 0 and y > 0:
    print('II четверть')
elif x < 0 and y < 0: \
    print('III четверть')
elif x > 0 and y < 0:
    print('IV четверть')

# 4. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат
# точек в этой четверти (x и y).

print('Введите номер четверти:')
quater = int(input())
if quater > 4 or quater < 1:
    print('Такой четверти нет')
elif quater == 1:
    print('x: (0; +∞)')
    print ('y: (0; +∞)')
elif quater == 2:
    print('x: (-∞; 0)')
    print('y: (0; +∞)')
elif quater == 3:
    print('x: (-∞; 0)')
    print('y: (-∞; 0)')
elif quater == 4:
    print('x: (0; +∞)')
    print('y: (-∞; 0)')

# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние
# между ними в 2D пространстве.

print('Введите координаты двух точек')
print ('a:')
x = int(input())
print ('b:')
y = int(input())
distance = x - y
if distance < 0:
    distance *= -1
print(distance)





