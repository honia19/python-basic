def parse_amount(input_string: str) -> str:
    normalized = ' '.join(input_string.strip().lower().split())

    parts = normalized.split()

    rubles = 0
    kopeks = 0

    try:
        if len(parts) == 2:
            if parts[1] in ['руб', 'рубль', 'рубля', 'рублей']:
                rubles = int(parts[0])
            else:
                return "Некорректный формат суммы"

        elif len(parts) == 4:
            if parts[1] in ['руб', 'рубль', 'рубля', 'рублей'] and \
                    parts[3] in ['коп', 'копейка', 'копейки', 'копеек']:
                rubles = int(parts[0])
                kopeks = int(parts[2])

                if kopeks < 0 or kopeks > 99:
                    return "Некорректный формат суммы"
            else:
                return "Некорректный формат суммы"
        else:
            return "Некорректный формат суммы"

        if rubles < 0:
            return "Некорректный формат суммы"

        return f"{rubles}.{kopeks:02d} ₽"

    except ValueError:
        return "Некорректный формат суммы"


user_input = input()
result = parse_amount(user_input)
print(result)
