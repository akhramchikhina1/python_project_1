import math
range_radius=int(input('Введите значение радиуса: '))
blind_radius=int(input('Введите значение радиуса: '))
area=abs(((range_radius **2) * math.pi)-((blind_radius **2) * math.pi))
print('Площадь покрываемой территории:', area)
