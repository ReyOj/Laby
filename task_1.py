money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

res = 0
rost = increase+1
while True:
    delt = spend - salary
    if delt > money_capital:
        break
    res += 1
    money_capital -= delt
    spend *= rost

print("Количество месяцев, которое можно протянуть без долгов:", res)