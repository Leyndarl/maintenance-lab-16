"""
Тесты для калькулятора
"""
import pytest
import sys
import os

# Добавляем путь к src для импорта
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.calculator import Calculator

class TestCalculator:
    """Класс с тестами для калькулятора"""
    
    def setup_method(self):
        """Создаем экземпляр калькулятора перед каждым тестом"""
        self.calc = Calculator()
    
    # Тесты для сложения
    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел"""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(10, 5) == 15
    
    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        assert self.calc.add(-2, -3) == -5
        assert self.calc.add(-5, 3) == -2
    
    def test_add_zero(self):
        """Тест сложения с нулем"""
        assert self.calc.add(0, 5) == 5
        assert self.calc.add(5, 0) == 5
        assert self.calc.add(0, 0) == 0
    
    # Тесты для вычитания
    def test_subtract_positive_numbers(self):
        """Тест вычитания положительных чисел"""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(10, 5) == 5
    
    def test_subtract_negative_numbers(self):
        """Тест вычитания отрицательных чисел"""
        assert self.calc.subtract(-2, -3) == 1
        assert self.calc.subtract(-5, 3) == -8
    
    # Тесты для умножения
    def test_multiply_positive_numbers(self):
        """Тест умножения положительных чисел"""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(4, 5) == 20
    
    def test_multiply_by_zero(self):
        """Тест умножения на ноль"""
        assert self.calc.multiply(5, 0) == 0
        assert self.calc.multiply(0, 5) == 0
    
    # Тесты для деления
    def test_divide_positive_numbers(self):
        """Тест деления положительных чисел"""
        assert self.calc.divide(6, 3) == 2
        assert self.calc.divide(10, 2) == 5
    
    def test_divide_by_zero(self):
        """Тест деления на ноль (должно вызывать исключение)"""
        with pytest.raises(ValueError) as exc_info:
            self.calc.divide(5, 0)
        assert str(exc_info.value) == "На ноль делить нельзя!"
    
    # Комбинированные тесты
    def test_multiple_operations(self):
        """Тест нескольких операций подряд"""
        result = self.calc.add(10, 5)  # 15
        result = self.calc.subtract(result, 3)  # 12
        result = self.calc.multiply(result, 2)  # 24
        result = self.calc.divide(result, 4)  # 6
        assert result == 6

# Отдельные функции для тестирования (не в классе)
def test_calculator_instance():
    """Тест создания экземпляра калькулятора"""
    calc = Calculator()
    assert isinstance(calc, Calculator)

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (0, 0, 0),
    (100, 200, 300),
])
def test_add_parametrized(a, b, expected):
    """Параметризованный тест сложения"""
    calc = Calculator()
    assert calc.add(a, b) == expected
