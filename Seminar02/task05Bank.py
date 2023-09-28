# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

summ = 1000
count = 0
RICHTAX = 0.9
RICHLIM = 5_000_000
BONUS = 1.03
COMISSIONPROC = 0.015
COMISSIONMIN = 30
COMISSIONMAX = 600
FREENDERING = 50
while True:
    action = input(
        f'Введите операцию:\n 1 - Пополнить \n 2 - Снять \n 3 - Выйти  ')
    if summ >= RICHLIM:
        summ *= RICHTAX
    if count % 3 == 0 and count != 0:
        summ *= BONUS
        count = 0
    if action == "1":
        in_cash = int(input('Введите сумму: '))
        if in_cash % FREENDERING == 0:
            summ += in_cash
            count += 1
            print(f' Вы внесли: {in_cash}  \n На вашем счете: {summ}')

    elif action == "2":
        out_cash = int(input('Введите сумму: '))
        if out_cash % FREENDERING == 0 and out_cash <= summ:
            comission = out_cash * 0.015
            if comission < COMISSIONMIN:
                comission = COMISSIONMIN
            elif comission > COMISSIONMAX:
                comission = COMISSIONMAX
            if (comission + out_cash) < summ:
                summ -= (comission + out_cash)
                count += 1
            print(
                f' Вы сняли: {out_cash} \n коммиссия: {comission} \n На вашем счете: {summ}')

    else:
        break
    print(summ)
