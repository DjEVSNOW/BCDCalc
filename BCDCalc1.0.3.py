# BCDCalc 1.0.3
# Программа для вычисления разницы в цене и процентах между двумя ценовыми величинами.# Окно приветствия с описанием назначения и функционалом.
#!/usr/bin/python3

print('\n '''' BCDCalc
Вычисления разницы в цене биржевых котировок. 
''')

# Интерактивная строка
try:
   num_1 = float(input('Первая цена:\n'))
   num_2 = float(input('Вторая цена:\n'))
except ValueError:
   print('Вы не ввели цифры! Перезапустите программу!')

# "Движок" программы.
quantity = num_1 / num_2 if num_1 > num_2 > 0.00001 else num_2 / num_1 
ext_difference = (num_1 - num_2) if num_1 > num_2 else num_2 - num_1 # $ расчет в валюте
procent_of_sum = ((num_2 * 100 / num_1) - 100) if num_2 <0.000001 else abs((num_1 * 100 /
num_2) - 100) # % проценты

# Вывод результата
print("\033[032m", "\n", "Изменение от первоночально заданной цены:", "\n",procent_of_sum, 
      "%","\n", "На", ext_difference, "$", "\n", "В", quantity, "раз") 

'''Author and Development by ---Puma---'''
