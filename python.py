print('Python'[1:4])    # 'yth'
print('Python'[1:1])    # ''
print('Python'[2:])     # 'thon'
print('Python'[:-2])    # 'Pyth'
print('Python'[:])      # 'Python'
print('Python'[0:6:2])  # 'Pto'

# Operaciones con cadenas
print('Me gusta ' + 'Python')       # 'Me gusta Python'
print('Python' * 3)                  # 'PythonPythonPython'
print('y' in 'Python')               # True
print('tho' in 'Python')             # True
print('to' not in 'Python')          # True

# Operaciones de comparación de cadenas
print('Python' == 'python')          # False
print('Python' < 'python')           # True
print('a' > 'Z')                     # True
print('A' >= 'Z')                    # False
print('' < 'Python')                 # True

# Funciones de cadenas
print(len('Python'))                 # 6
print(min('Python'))                 # 'P'
print(max('Python'))                 # 'y'
print('Python'.upper())              # 'PYTHON'
print('A,B,C'.split(','))            # ['A', 'B', 'C']
print('I love Python'.split())       # ['I', 'love', 'Python']

# Cadenas formateadas (format())
print('Un {} vale {} {}'.format('€', 1.12, '$'))                             # 'Un € vale 1.12 $'
print('Un {2} vale {1} {0}'.format('€', 1.12, '$'))                           # 'Un $ vale 1.12 €'
print('Un {moneda1} vale {cambio} {moneda2}'.format(moneda1='€', cambio=1.12, moneda2='$')) # 'Un € vale 1.12 $'
print('Hoy es {:^10}, mañana {:10} y pasado {:>10}'.format('lunes', 'martes', 'miércoles')) # 'Hoy es lunes , mañana martes y pasado miércoles'
print('Cantidad {:5d}'.format(12))                                           # 'Cantidad 12'
print('Pi vale {:8.4f}'.format(3.141592))                                     # 'Pi vale 3.1416'DDD

# Datos lógicos o booleanos (clase bool)
print(not True)                      # FalseD
print(True and False)                # False
print(True and True)                 # True

# Conversión de datos primitivos simples
print(int('12'))                     # 12
print(int(True))                     # 1
# print(int('c'))                    # Error

print(float('3.14'))                 # 3.14
print(float(True))                   # 1.0
# print(float('III'))                # Error

print(str(3.14))                     # '3.14'
print(str(True))                     # 'True'

print(bool('0'))                     # False
print(bool('3.14'))                  # True
print(bool(''))                      # False
print(bool('Hola'))                  # True

# Entrada por terminal (input())
language = input('?`Cuál es tu lenguaje favorito? ')
print(language)                      # 'Python'

age = input('?`Cuál es tu edad? ')
print(age)                           # '20'

# Salida por terminal (print())
print('Hola')                        # 'Hola'
name = 'Alf'
print('Hola', name)                  # 'Hola Alf'
print('El valor de pi es', 3.1415)   # 'El valor de pi es 3.1415'
print('Hola', name, sep='')          # 'HolaAlf'
print('Hola', name, end='!\n')       # 'Hola Alf!'

# Estructuras de control
# Condicionales (if)
if True:
    print("Esta condición se cumple")

# Bucles condicionales (while)
i = 0
while i < 5:
    print(i)
    i += 1

# Bucles iterativos (for)
for i in range(5):
    print(i)