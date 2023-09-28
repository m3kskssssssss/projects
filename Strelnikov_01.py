print('Введите первое число:')
pervoe_chislo = int(input())
print('Введите второе число:')
vtoroe_chislo = int(input())
print('Сумма:' + str(pervoe_chislo + vtoroe_chislo))
print('Разность:' + str(pervoe_chislo - vtoroe_chislo))
print('Произведение:' + str(pervoe_chislo * vtoroe_chislo))
print('Среднее арифметическое:' + str((pervoe_chislo + vtoroe_chislo)/2))
if pervoe_chislo > vtoroe_chislo:
    print('Разность максимума и минимума:' + str(pervoe_chislo - vtoroe_chislo))
else:
    print('Разность максимума и минимума:' + str(vtoroe_chislo - pervoe_chislo))