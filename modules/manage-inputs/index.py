def find_largest_number():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    if (num1 > num2) and (num1 > num3):
        max_num = num1
    elif (num2 > num1) and (num2 > num3):
        max_num = num2
    elif (num3 > num1) and (num3 > num2):
        max_num = num3
    else:
        print("There is a tie for the largest number.")
        return
    print(f"The largest number is: {max_num}")


def elevator() -> None:
    floor = int(input("Enter the floor number (-1 to 10): "))

    match floor:
        case -1: print("Going to the basement.")
        case 1: print("You are on the ground floor.")
        case _ if 2 <= floor <= 9:
            if floor % 2 == 0:
                print(
                    f"Going to floor {floor}, which is an even-numbered floor.")
            else:
                print(
                    f"Going to floor {floor}, which is an odd-numbered floor.")
        case 10: print("Going to the top floor.")
        case _: print("Invalid floor number.")


rating = int(input("Введите рейтинг фильма (1-10): "))

if 1 <= rating <= 3:
    result = "Плохой фильм"
elif 4 <= rating <= 7:
    result = "Средний фильм"
elif 8 <= rating <= 10:
    result = "Отличный фильм"
else:
    result = "Неверный рейтинг"

print(result)


role = input("Введите роль пользователя: ")

match  role:
    case 'admin':
        access_rights = "Полный доступ ко всем функциям"
    case 'moderator':
        access_rights = "Частичный доступ"
    case 'user':
        access_rights = "Ограниченный доступ"
    case 'guest':
        access_rights = "Доступ только для чтения"
    case _:
        access_rights = "Неизвестная роль"

print(access_rights)


amount = float(input())

if (amount > 0 and amount < 1000):
    print(amount)
elif (1000 <= amount and amount <= 5000):
    discount = amount * 0.05
    final_amount = amount - discount
    print(final_amount)
else:
    discount = amount * 0.10
    final_amount = amount - discount
    print(final_amount)


grade = int(input())

match grade:
    case _ if grade >= 90 and grade <= 100: result = "Лучшая работа"
    case _ if 80 <= grade < 90: result = "Отличная работа"
    case _ if grade < 80 and grade >= 60: result = "Удовлетворительная работа"
    case _: result = "Нужно подтянуть знания"

print(result)


wheels = int(input())

match wheels:
    case 2: result = "Мотоцикл"
    case 4: result = "Автомобиль"
    case 6: result = "Грузовик"
    case _: result = "Неизвестный транспорт"

print(result)

order_id = int(input())

if 1000 <= order_id <= 1999:
    status = "Заказ в обработке"
elif 2000 <= order_id <= 4999:
    status = "Заказ отправлен"
elif 5000 <= order_id <= 7999:
    status = "Заказ доставлен"
elif 8000 <= order_id <= 9999:
    status = "Заказ отменен"
else:
    status = "Неверный номер заказа"

print(status)


chest_size = int(input())

if 70 <= chest_size < 88:
    size = "S"
elif 88 <= chest_size < 96:
    size = "M"
elif 96 <= chest_size < 102:
    size = "L"
elif 102 <= chest_size <= 130:
    size = "XL"
else:
    size = "Invalid chest size"

print(size)

password = input("Введите пароль: ")

if password == "admin123":
    access_level = "Администраторский доступ"
elif password == "user":
    access_level = "Пользовательский доступ"
elif password == "guest":
    access_level = "Гостевой доступ"
else:
    access_level = "Неизвестный уровень доступа"

print(access_level)

importance = 'high'
urgency = 'high'

# Словарь приоритетов: (важность, срочность) -> приоритет
priority_map = {
    ('high', 'high'): "Критический приоритет",
    ('high', 'medium'): "Высокий приоритет",
    ('high', 'low'): "Средний приоритет",
    ('medium', 'high'): "Высокий приоритет",
    ('medium', 'medium'): "Средний приоритет",
    ('medium', 'low'): "Низкий приоритет",
    ('low', 'high'): "Средний приоритет",
    ('low', 'medium'): "Низкий приоритет",
    ('low', 'low'): "Очень низкий приоритет"
}

priority = priority_map.get((importance, urgency), "Неизвестный приоритет")

print(priority)
