product_price = int(input("Введите цену продукта: "))
discount_percentage = int(input("Введите процент скидки: "))

calculate_price_with_discount = product_price - (product_price * discount_percentage / 100)

print("Цена с учетом скидки:", calculate_price_with_discount)
