print("Введите количество билетов, которые Вы хотите приобрести на мероприятие")
tick_s = int(input("> "))
sum_tick = 0

for i in range(1, tick_s+1):
    print("Введите возраст", i, "-го посетителя")
    tick_age = int(input("> "))
    if tick_age < 18:
        print("Стоимость билета", i, "-го посетителя - 0 руб.")
    elif 18 >= tick_age < 25:
        print("Стоимость билета", i, "-го посетителя - 990 руб.")
        sum_tick += 990
    else:
        print("Стоимость билета", i, "-го посетителя - 1390 руб.")
        sum_tick += 1390
print("Сумма без скидки", sum_tick, "руб.")

if tick_s > 3:
    print("Ваша скидка на мероприятие - 10%")
    sum_tick = int(round(sum_tick * (100-10)/100))

print("Сумма к оплате", sum_tick, "руб.")
