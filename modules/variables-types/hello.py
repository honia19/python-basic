import keyword
import re
from typing import Any


def is_valid_variable_name(name: str) -> bool:
    if len(name) == 0 or len(name) > 50:
        return False

    if not name.isascii():
        return False

    if not name.isidentifier() or keyword.iskeyword(name):
        return False

    return True


print(is_valid_variable_name("valid_name"))  # True
print(is_valid_variable_name(""))            # False
print(is_valid_variable_name("a" * 51))      # False
print(is_valid_variable_name("válid_name"))  # False
print(is_valid_variable_name("1invalid"))    # False
print(is_valid_variable_name("for"))         # False

print(int(12.9))


def describe_type(value: int | float | str | bool) -> str:
    return f"Тип: {type(value).__name__}"


print(describe_type(42))          # The type of the value is int


def repeat_string(text: str, count: int) -> str:
    return text * count


print(repeat_string("abc", 3))  # "abcabcabc"
print(repeat_string("xyz", 0))  # ""
print(repeat_string("!", -2))   # ""


def format_type_annotations(text: str, number: int) -> str:
    return f"text: str = '{text}', number: int = {number}"


def convert_to_string(value: int | float | str | bool) -> str:
    return str(value)


def is_python_file(filename: str) -> bool:
    return filename.endswith(".py")


def is_valid_constant_name(constant_name: str) -> bool:
    if not constant_name.isidentifier():
        return False

    if not re.match(r'^[A-Z0-9_]+$', constant_name):
        return False

    if not re.search(r'[A-Z]', constant_name):
        return False

    return True


print(is_valid_constant_name("MAX_VALUE"))  # True
print(is_valid_constant_name("max_value"))  # False
print(is_valid_constant_name("MAX-VALUE"))  # False
print(is_valid_constant_name("123_CONSTANT"))  # False


def evaluate_expression(expression: str) -> float:
    parts = expression.split()

    if len(parts) != 3:
        raise ValueError("Invalid expression format")

    [num1_str, operator, num2_str] = parts

    try:
        num1 = float(num1_str)
        num2 = float(num2_str)
    except ValueError:
        raise ValueError("Invalid number format")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        result = num1 / num2
    else:
        raise ValueError(f"Unknown operator: {operator}")

    if result.is_integer():
        return int(result)
    else:
        return result


print("    3    + 5      ".strip().split())        # 8


def analyze_variables(variables: list[tuple[str, Any]]) -> dict[str, str]:
    result: dict[str, str] = {}

    for key, value in variables:
        result[key] = type(value).__name__

    return result

    # Input: ["UserAge", "firstName", "IsActive"]
    # Output: {"UserAge": "user_age", "firstName": "first_name",
    # "IsActive": "is_active"}
    #
    # Input: ["totalCount", "MaxValue"]
    # Output: {"totalCount": "total_count", "MaxValue": "max_value"}


def convert_to_snake_case(variables: list[str]) -> dict[str, str]:
    result: dict[str, str] = {}

    for var in variables:
        snake_case = re.sub(r'(?<!^)(?=[A-Z])', '_', var).lower()
        result[var] = snake_case

    return result
