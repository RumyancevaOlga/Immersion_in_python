# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные
# операции — функции. Дополнительно сохраняйте все операции поступления и снятия
# средств в список.

MINIMUM_BILL = 50
PERCENT = 0.015
LOW_LIMIT = 30
UP_LIMIT = 600
THIRD_PERCENT = 0.03
WEALTH_TAX = 0.1

operation = True
balance = 0


def is_bill() -> int:
    check = True
    cash = 0
    while check:
        cash = int(input('Введите сумму: '))
        if cash % MINIMUM_BILL == 0:
            check = False
        else:
            print('Ошибка! Сумма не кратна', MINIMUM_BILL)
    return cash


def deposit(balance: int) -> int:
    cash = is_bill()
    print(balance, '+', cash)
    balance += cash
    contorol('Внесение наличных', str(cash))
    return balance


def withdrawal(balance: int) -> int:
    cash = is_bill()
    percents = 0
    if LOW_LIMIT <= balance * PERCENT < UP_LIMIT:
        percents = balance * PERCENT
    elif balance * PERCENT < LOW_LIMIT:
        percents = LOW_LIMIT
    else:
        percents = UP_LIMIT
    if balance + percents >= cash:
        print(balance, '-', percents, '-', cash)
        balance -= percents + cash
        contorol('Снятие наличных', str(cash) + ' процент за операцию ' + str(percents))
    else:
        print('Ошибка! Сума списания превышает баланс.')
    return balance


def is_reach(balance: int) -> int:
    if balance >= 5_000_000:
        print('Снятие налога на богатство.')
        print(balance, '-', balance * WEALTH_TAX)
        balance -= balance * WEALTH_TAX
        contorol('Снятие налога на богатство', str(balance * WEALTH_TAX))
    return balance


def menu() -> str:
    print('Для снятия наличных нажмите введите 1')
    print('Для внесения наличных введите 2')
    print('Для выхода введите 3')
    return input()


def contorol(operation: str, money: str):
    global list_control
    list_control.append([operation, money])


count = 0
list_control = []

while operation:
    count += 1
    balance = is_reach(balance)
    num = menu()
    if num == '1':
        balance = withdrawal(balance)
    elif num == '2':
        balance = deposit(balance)
    elif num == '3':
        operation = False
    else:
        print('Ошибка! Некорректный ввод.')
    if count % 3 == 0:
        print('Пополнение баланса на 3 процента')
        print(balance, '+', balance * THIRD_PERCENT)
        balance += balance * THIRD_PERCENT
        contorol('Пополнение за третью операцию', str(balance * THIRD_PERCENT))
    print('Текущий баланс равен', balance)

print(list_control)