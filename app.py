#!/usr/bin/env python3
"""
Главный файл приложения
Демонстрация работы калькулятора
"""

from src.calculator import Calculator, main

def run_demo():
    """Запуск демонстрации"""
    print("=" * 40)
    print("ДЕМОНСТРАЦИЯ РАБОТЫ КАЛЬКУЛЯТОРА")
    print("=" * 40)
    
    calc = Calculator()
    
    # Интерактивный режим
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")
        
        choice = input("Ваш выбор (1-5): ")
        
        if choice == '5':
            print("До свидания!")
            break
        
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            
            if choice == '1':
                result = calc.add(a, b)
                print(f"{a} + {b} = {result}")
            elif choice == '2':
                result = calc.subtract(a, b)
                print(f"{a} - {b} = {result}")
            elif choice == '3':
                result = calc.multiply(a, b)
                print(f"{a} * {b} = {result}")
            elif choice == '4':
                result = calc.divide(a, b)
                print(f"{a} / {b} = {result}")
            else:
                print("Неверный выбор!")
                
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

if __name__ == "__main__":
    # Запускаем демо или основную функцию
    mode = input("Запустить демо? (y/n): ").lower()
    if mode == 'y':
        run_demo()
    else:
        main()
