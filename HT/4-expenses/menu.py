def add_expense(expenses: list[float], value: str) -> bool:
    """Добавляет расход в список"""
    try:
        amount: float = float(value)
        if amount <= 0:
            print("Ошибка: сумма должна быть положительной")
            return False
        expenses.append(amount)
        print(f"Расход {amount} добавлен успешно!")
        return True
    except ValueError:
        print("Ошибка: введите корректное число")
        return False


def delete_expense(expenses: list[float], index: str) -> bool:
    """Удаляет расход по индексу"""
    try:
        index_int: int = int(index) - 1  # Преобразуем в индекс (начиная с 0)
        if 0 <= index_int < len(expenses):
            removed: float = expenses.pop(index_int)
            print(f"Расход {removed} удален успешно!")
            return True
        else:
            print("Ошибка: неверный номер расхода")
            return False
    except ValueError:
        print("Ошибка: введите корректный номер")
        return False


def get_total(expenses: list[float]) -> float:
    """Возвращает общую сумму расходов"""
    return sum(expenses)


def get_average(expenses: list[float]) -> float:
    """Возвращает средний расход"""
    if len(expenses) == 0:
        return 0
    return sum(expenses) / len(expenses)


def print_report(expenses: list[float]) -> None:
    """Печатает красивый отчёт о расходах"""
    print("\n" + "="*40)
    print("          ОТЧЁТ О РАСХОДАХ")
    print("="*40)

    if not expenses:
        print("Расходы отсутствуют")
    else:
        print(f"\n{'№':<5} {'Сумма':<15}")
        print("-" * 40)
        for i, expense in enumerate(expenses, 1):
            print(f"{i:<5} {expense:<15.2f}")
        print("-" * 40)
        print(f"\nВсего расходов: {len(expenses)}")
        print(f"Общая сумма: {get_total(expenses):.2f}")
        print(f"Средний расход: {get_average(expenses):.2f}")
    print("="*40 + "\n")


expenses: list[float] = []

while True:
    print("\n=== Меню управления расходами ===")
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")

    choice: str = input("\nВыберите действие (1-5): ")

    if choice == "5":
        print("До свидания!")
        break
    elif choice == "1":
        value: str = input("Введите сумму расхода: ")
        add_expense(expenses, value)
    elif choice == "2":
        print_report(expenses)
    elif choice == "3":
        if not expenses:
            print("Расходы отсутствуют")
        else:
            print(f"\nОбщая сумма: {get_total(expenses):.2f}")
            print(f"Средний расход: {get_average(expenses):.2f}")
    elif choice == "4":
        if not expenses:
            print("Список расходов пуст")
        else:
            print_report(expenses)
            index: str = input("Введите номер расхода для удаления: ")
            delete_expense(expenses, index)
    else:
        print("Неверный выбор. Попробуйте снова.")
