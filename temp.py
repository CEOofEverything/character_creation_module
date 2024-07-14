from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для вычисления '
                'квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Вызывает функцию для вычисления квадратного корня."""
    if your_number <= 0:
        return print('Число <= 0')
    result = calculate_square_root(your_number)
    return print(('Мы вычислили квадратный корень из введённого вами числа. '
                  f'Это будет: {result}'))


print(message)
calc(25.5)
