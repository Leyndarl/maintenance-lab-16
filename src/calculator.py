"""
Модуль калькулятора для демонстрации CI/CD
"""

class Calculator:
    """Простой калькулятор"""
    
    @staticmethod
    def add(a, b):
        """Сложение"""
        return a + b
    
    @staticmethod
    def subtract(a, b):
        """Вычитание"""
        return a - b
    
    @staticmethod
    def multiply(a, b):
        """Умножение"""
        return a * b
    
    @staticmethod
    def divide(a, b):
        """Деление"""
        if b == 0:
            raise ValueError("На ноль делить нельзя!")
        return a / b

def main():
    """Пример использования"""
    calc = Calculator()
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")

if __name__ == "__main__":
    main()
