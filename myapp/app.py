def add(num1: int | float, num2: int | float) -> int | float:
    return num1 + num2


def subtract(num1: int | float, num2: int | float) -> int | float:
    return num1 - num2


if __name__ == "__main__":
    number1 = 10
    number2 = 20
    print(f"Add {number1}, {number2} = {add(number1, number2)}")
    print(f"Subtract {number1}, {number2} = {subtract(number1, number2)}")
