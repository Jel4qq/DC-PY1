money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# TODO Оформить решение
#  в месяц денег money_capital+salary обозначим capital
#  тратим в первый месяц spend в последующие spend*(1+increase)
#  остаток обозначим ost_
capital = money_capital+salary
while capital > 0:
    capital = capital - spend
    spend = spend * 1.05
    month += 1

print(month)
