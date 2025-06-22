money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
current_capital = money_capital

while True:
    if current_capital + salary >= spend:
        current_capital = current_capital + salary - spend
        spend *= (1 + increase)
        months += 1
    else:
        break

print("Количество месяцев, которое можно протянуть без долгов:", months)