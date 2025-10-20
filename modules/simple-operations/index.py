def compare_numbers(a: int, b: int) -> str:
    if a > b:
        return "first_greater"
    elif a < b:
        return "second_greater"
    else:
        return "equal"
    

def calculate_expression(x: int | float) -> int | float:
    return x ** 2 + 3 * x - 5

print(calculate_expression(2))
print(calculate_expression(-1))

def apply_assignment_operations(initial_value: int | float) -> int | float:
    return (initial_value + 10) * 2 - 5

print(apply_assignment_operations(5))
print(apply_assignment_operations(0))

def logical_operations(a: bool, b: bool) -> tuple[bool, bool, bool]:
    is_and = a and b
    is_or = a or b
    is_not_a = not a

    return (is_and, is_or, is_not_a)

def calculate_expression1(x: int | float) -> int | float:
    return 2 + x * 3 ** 2 - 4

print(calculate_expression1(1))
print(calculate_expression1(0))

def count_characters(text: str) -> int:
    return len(text)

def bitwise_operations(value: int) -> int:
    b_or = value | 12
    b_and = b_or & 15
    return b_and ^ 7

print(bitwise_operations(8))
print(bitwise_operations(5))

def count_above_average(numbers: list[int]) -> int:
    average = sum(numbers) / len(numbers)
    count: int = 0
    
    for num in numbers:
        count += num > average

    return count

print(count_above_average([1, 2, 3, 4, 5]))
print(count_above_average([10, 10, 10]))

def calculate_sqrt_product(a: int | float, b: int | float) -> float:
    return (a * b) ** 0.5

print(calculate_sqrt_product(4, 9))
print(calculate_sqrt_product(2, 8))

def complex_logic(p: bool, q: bool) -> bool:
    return not (p and q) or (p or not q)