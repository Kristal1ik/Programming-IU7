#  Если для подстановки требуется только один аргумент, то значение - сам аргумент:
print('Hello, {}!'.format('Vasya'))  # Hello, Vasya!

#  А если несколько, то значениями будут являться все аргументы со строками подстановки (обычных или именованных):
print('{0}, {1}, {2}'.format('a', 'b', 'c'))  # a, b, c
print('{}, {}, {}'.format('a', 'b', 'c'))  # a, b, c
print('{2}, {1}, {0}'.format('a', 'b', 'c'))  # c, b, a
print('{2}, {1}, {0}'.format(*'abc'))  # c, b, a
print('{0}{1}{0}'.format('abra', 'cad'))  # abracadabra
print('Coordinates: {latitude}, {longitude}'.format(latitude='37.24N',
                                                    longitude='-115.81W'))  # Coordinates: 37.24N, -115.81W
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
print('Coordinates: {latitude}, {longitude}'.format(**coord))  # Coordinates: 37.24N, -115.81W

#  Дополнительный синтаксис format
'''поле замены     ::=  "{" [имя поля] ["!" преобразование] [":" спецификация] "}"
имя поля        ::=  arg_name ("." имя атрибута | "[" индекс "]")*
преобразование  ::=  "r" (внутреннее представление) | "s" (человеческое представление)
спецификация    ::=  см. ниже'''

print("Units destroyed: {players[0]}".format(players=[1, 2, 3]))  # Units destroyed: 1
print("Units destroyed: {players[0]!r}".format(players=['1', '2', '3']))  # Units destroyed: '1'

#  Спецификация format
'''
спецификация ::=  [[fill]align][sign][#][0][width][,][.precision][type]
заполнитель  ::=  символ кроме '{' или '}'
выравнивание ::=  "<" | ">" | "=" | "^"
знак         ::=  "+" | "-" | " "
ширина       ::=  integer
точность     ::=  integer
тип          ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" |
                  "n" | "o" | "s" | "x" | "X" | "%"
'''

#  Выравнивание производится при помощи символа-заполнителя. Доступны следующие варианты выравнивания:

'''
Флаг	Значение
'<'	    Символы-заполнители будут справа (выравнивание объекта по левому краю) (по умолчанию).
'>'	    выравнивание объекта по правому краю.
'='	    Заполнитель будет после знака, но перед цифрами. Работает только с числовыми типами.
'^'	    Выравнивание по центру.
'''

#  Опция "знак" используется только для чисел и может принимать следующие значения:
'''
Флаг	Значение
'+'	    Знак должен быть использован для всех чисел.
'-'	'-' для отрицательных, ничего для положительных.
'Пробел'	'-' для отрицательных, пробел для положительных.
'''

#  Поле "тип" может принимать следующие значения:
'''
Тип	            Значение
'd', 'i', 'u'	Десятичное число.
'o'	            Число в восьмеричной системе счисления.
'x'	            Число в шестнадцатеричной системе счисления (буквы в нижнем регистре).
'X'	            Число в шестнадцатеричной системе счисления (буквы в верхнем регистре).
'e'	            Число с плавающей точкой с экспонентой (экспонента в нижнем регистре).
'E'	            Число с плавающей точкой с экспонентой (экспонента в верхнем регистре).
'f', 'F'	    Число с плавающей точкой (обычный формат).
'g'	            Число с плавающей точкой. с экспонентой (экспонента в нижнем регистре), если она меньше, чем -4 или точности, иначе обычный формат.
'G'	            Число с плавающей точкой. с экспонентой (экспонента в верхнем регистре), если она меньше, чем -4 или точности, иначе обычный формат.
'c'	            Символ (строка из одного символа или число - код символа).
's'	            Строка.
'%'	            Число умножается на 100, отображается число с плавающей точкой, а за ним знак %.
'''

#  Примеры:

coord = (3, 5)
print('X: {0[0]};  Y: {0[1]}'.format(coord))  # X: 3;  Y: 5

print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1',
                                                              'test2'))  # repr() shows quotes: 'test1'; str() doesn't: test2

print('{:<30}'.format('left aligned'))  # 'left aligned                  '

print('{:>30}'.format('right aligned'))  # '                 right aligned'

print('{:^30}'.format('centered'))  # '           centered           '

# Использование '*' как знак-заполнитель
print('{:*^30}'.format('centered'))  # '***********centered***********'

#  Всегда показывать знак перед числом
print('{:+f}; {:+f}'.format(3.14, -3.14))  # '+3.140000; -3.140000'

#  Указание пробела перед положительными числами
print('{: f}; {: f}'.format(3.14, -3.14))  # ' 3.140000; -3.140000'

#  Показывать только минус перед знаком, эквивалентно {:f}; {:f}'
print('{:-f}; {:-f}'.format(3.14, -3.14))  # '3.140000; -3.140000'

# format также поддерживает бинарные числа
print("int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42))  # 'int: 42;  hex: 2a;  oct: 52;  bin: 101010'

# Можно даже показывать префиксы: 0x, 0o, or 0b as prefix
print("int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(
    42))  # 'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

#  Вычисления в выводе!!
points = 19.5
total = 22
print('Correct answers: {:.2%}'.format(points / total))  # 'Correct answers: 88.64%'

#  Можем засунуть массив и обращаться по индексу элемента
print("{aux[1]:>{aux[0]}}\n {aux[2]:>{aux[0]}}>\n".format(aux=[82, 'y', 82 * '-']))