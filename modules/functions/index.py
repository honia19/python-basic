from typing import Any, Literal
from string import ascii_letters, digits
from random import choice


def generate_password(length: int = 8, use_symbols: bool = True) -> str:
    if length < 3:
        return ""
    symbols: Literal['!@#$%^&*?'] = '!@#$%^&*?'
    pool = ascii_letters + digits

    if use_symbols:
        pool += symbols

    password_chars: list[str] = []

    while len(password_chars) < length:
        password_chars.append(choice(pool))

    return "".join(password_chars)


# print(generate_password(20, True))
# print(generate_password(use_symbols=False))

def calculate_delivery_cost(weight: float, distance: int, delivery_type: Literal['standard', 'express', 'overnight'], insurance: bool = False) -> float:
    """
    Рассчитывает стоимость доставки товара

    :param weight: вес товара в килограммах
    :param distance: расстояние доставки в километрах
    :param delivery_type: тип доставки
    :param insurance: нужна ли страховка
    :return: итоговая стоимость доставки
    """

    DEFAULT_DELIVERY_COST = 100.0
    PRICE_PER_KG = 15.0
    PRICE_PER_KM = 2.0
    INSURANCE_RATE = 1.10

    base_cost_per_km = {
        'standard': 1.0,
        'express': 1.5,
        'overnight': 2.0
    }

    if delivery_type not in base_cost_per_km:
        raise ValueError(
            f"Неверный тип доставки: {delivery_type}. Допустимые значения: 'standard', 'express', 'overnight'")

    base_cost_without_multiplier = DEFAULT_DELIVERY_COST + \
        weight * PRICE_PER_KG + distance * PRICE_PER_KM

    base_cost = base_cost_without_multiplier * base_cost_per_km[delivery_type]

    cost = base_cost * INSURANCE_RATE if insurance else base_cost

    return round(cost, 2)


# print(calculate_delivery_cost(1.0, 100, 'express', True))

def find_maximum(*args: int, ignore_negative: bool = False) -> float | None:
    filtered_elements: list[int] = []

    for elem in args:
        if ignore_negative and elem < 0:
            continue
        else:
            filtered_elements.append(elem)

    if not filtered_elements:
        return None

    return max(filtered_elements)


# print(find_maximum(-3, -1, -5, ignore_negative=True))
# print(find_maximum(5, 2, 8, 1))
# print(find_maximum(5, 2, -8, 1))

def validate_user_data(user_data: dict[str, Any], required_fields: list[str], strict_mode: bool = False) -> bool:
    """
    Валидация структуры данных пользователя

    :param user_data: словарь с данными пользователя
    :param required_fields: список обязательных полей
    :param strict_mode: строгий режим проверки
    :return: результат валидации
    """
    if strict_mode:
        if set(user_data.keys()) != set(required_fields):
            return False

    for field in required_fields:
        if field not in user_data:
            return False

        value = user_data[field]

        if value is None:
            return False

        if isinstance(value, str) and value.strip() == '':
            return False

    return True


print(validate_user_data(
    {'name': 'John', 'email': 'john@test.com'}, ['name', 'email', 'key']))

print(validate_user_data({'name': 'John', 'age': 25},
      ['name', 'email'], strict_mode=True))
