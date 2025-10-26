expenses_weekly = [250, 150, 400, 100, 350, 200, 300]

total_expenses = sum(expenses_weekly)
average_expense = total_expenses / len(expenses_weekly)
min_expense = min(expenses_weekly)
max_expense = max(expenses_weekly)

print((min_expense, max_expense, total_expenses))
