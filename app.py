def add(a, b):
    """Складывает два числа"""
    return a + b

def subtract(a, b):
    """Вычитает второе число из первого"""
    return a - b

def multiply(a, b):
    """Умножает два числа"""
    return a * b

def divide(a, b):
    """Делит первое число на второе"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

if __name__ == "__main__":
    print("Калькулятор работает!")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 3 = {multiply(4, 3)}")
    print(f"10 / 2 = {divide(10, 2)}")