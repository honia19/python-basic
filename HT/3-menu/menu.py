category = input("Выберите категорию (напиток/суп/десерт): ").lower()

match category:
    case "напиток":
        print("Доступные напитки: чай, кофе, сок")
        drink = input("Выберите напиток: ").lower()

        match drink:
            case "чай":
                price = 50
            case "кофе":
                price = 120
            case "сок":
                price = 80
            case _:
                price = None
                print("Неизвестный напиток")

        if price:
            print(f"Цена: {price} $")

    case "суп":
        print("Доступные супы: борщ, щи, суп-пюре")
        soup = input("Выберите суп: ").lower()

        match soup:
            case "борщ":
                price = 150
            case "щи":
                price = 130
            case "суп-пюре":
                price = 180
            case _:
                price = None
                print("Неизвестный суп")

        if price:
            print(f"Цена: {price} $")

    case "десерт":
        print("Доступные десерты: торт, мороженое, фрукты")
        dessert = input("Выберите десерт: ").lower()

        match dessert:
            case "торт":
                price = 200
            case "мороженое":
                price = 90
            case "фрукты":
                price = 100
            case _:
                price = None
                print("Неизвестный десерт")

        if price:
            print(f"Цена: {price} $")

    case _:
        print("Неизвестная категория")
