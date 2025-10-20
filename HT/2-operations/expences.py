expenses_food = int(input("Введите ваши расходы на еду: "))
expenses_transport = int(input("Введите ваши расходы на транспорт: "))
expenses_entertainment = int(input("Введите ваши расходы на развлечения: "))

common_expenses = expenses_food + expenses_transport + expenses_entertainment
average_expenses = common_expenses / 3

print("Общие расходы:", common_expenses)
print("Средние расходы:", average_expenses)
