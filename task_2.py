salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

res = 0
rost = increase+1
for i in range(months):
      res += spend - salary
      spend *= rost

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(res))
