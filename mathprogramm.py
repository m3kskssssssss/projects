pervoe_chislo_modul = 0
vtoroe_chislo_modul = 0
chastnoe = 0



print('Введите первое число:')
pervoe_chislo = int(input())
print('Введите второе число:')
vtoroe_chislo = int(input())
print('Введите математический знак: +, -, *, /, srednee_arifm, raznica_moduley')
deystviye = input()



if deystviye == '+':
    print('Сумма двух чисел: ' + str(pervoe_chislo + vtoroe_chislo))
elif deystviye == '-':
    print('Разность двух чисел: ' + str(pervoe_chislo - vtoroe_chislo))
elif deystviye == '*':
    print('Произведение двух чисел: ' + str(pervoe_chislo * vtoroe_chislo))
elif deystviye == 'srednee_arifm':
    print('Среднее арифметическое двух чисел: ' + str((pervoe_chislo + vtoroe_chislo)/2))
elif deystviye == 'raznica_moduley':
    if pervoe_chislo >= 0:
        pervoe_chislo_modul = pervoe_chislo
    else:
        pervoe_chislo_modul = - pervoe_chislo
    if vtoroe_chislo >= 0:
        vtoroe_chislo_modul = vtoroe_chislo
    else:
        vtoroe_chislo_modul = - vtoroe_chislo
    if pervoe_chislo_modul >= vtoroe_chislo_modul:
        print('Разница модулей двух чисел равна: ' + str(pervoe_chislo_modul - vtoroe_chislo_modul))
    else:
        print('Разница модулей двух чисел равна: ' + str(vtoroe_chislo_modul - pervoe_chislo_modul))
elif deystviye == '/':
    chastnoe = pervoe_chislo / vtoroe_chislo
    print(f"{chastnoe:.2f}")
else:
    print('Неверно указано необходимое математическое действие или число. Перезапустите программу.')
