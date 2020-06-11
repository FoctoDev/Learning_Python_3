# Operators
print('2. ', 3 + 5) # Суммирует два объекта
print('3. ', 'a' + 'b') # Суммирует два объекта

print('5. ', -5.2) # Даёт разность двух чисел
print('6. ', 50 - 24) # Даёт разность двух чисел

print('8. ', 2 * 3) # Даёт произведени двух чисел
print('9. ', 'la' * 3) # Возвращет строку, повторённую заданное число раз

print('11. ', 3 ** 4) # Возвращает число x, возведённое в степень y

print('13. ', 4 / 3) # Возвращает частное от деления x на y

print('15. ', 4 // 3) # Возвращает неполное частное от деления
print('16. ', -4 // 3) # Возвращает неполное частное от деления

print('18. ', 8 % 3) # Возвращает остаток от деления

print('20. ', 2 << 2) # Сдвиагет биты числа влево на заданное поличество позиций

print('22. ', 11 >> 1) # Сдвиагет биты числа вправо на заданное поличество позиций

print('24. ', 5 & 3) # Побитовая операция И над числами

print('26. ', 5 | 3) # Побитовая операция ИЛИ над числами

print('28. ', 5 ^ 3) # Побитовая операция ИСКЛЮЧИТЕЛЬНО ИЛИ

print('30. ', ~5) # Побитовая операция НЕ для числа x соответствует -(x+1)

print('32. ', 5 < 3, 3 < 5, 3 < 5 < 7) # Определяет верно ли что x меньше y

print('34. ', 5 > 3, 3.5 > 5) # Определяет верно ли что x больше y

x = 3
y = 6
print('38. ', x <= y) # Определяет верно ли что x меньше или равно y

x = 4
y = 3
print('42. ', x >= y) # Определяет верно ли что x больше или равно y

x = 2
y = 2
print('46. ', x == y) # Проверяет, одинаковы ли объекты

x = 'str'
y = 'stR'
print('50. ', x == y) # Проверяет, одинаковы ли объекты

x = 2
y = 3
print('54. ', x != 3) # Проверяет, верно ли что объекты не равны

x = True
print('50. ', not x) # Если x равно True, оператор вернёт False

x = False
y = True
print('50. ', x and y) # x and y даёт False, если x равно False, в противном случае возвращает значение y

x = True
y = False
print('50. ', x or y) # Если x равно True, в результате получим True, в противном случае получим значение y

a = 2
a += 1 # или a = a + 1
print(a)

b = 3
b -= 2 # или b = b - 2
print(b)

c = 4
c *= 2 # или c = c * 2
print(c)

d = 10
d /= 2 # или d = d / 2
print(d)
