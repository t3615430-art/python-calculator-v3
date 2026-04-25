# Третя версія: Консольний калькулятор з історією операцій та збереженням у файл
# Script Master - Python Portfolio

import os

HISTORY_FILE = "calculator_history.txt"
history = []

def load_history():
    """Завантажує історію з файлу при старті"""
    global history
    if os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                history = [line.strip() for line in f.readlines() if line.strip()]
        except:
            history = []

def save_history():
    """Зберігає історію у файл"""
    try:
        with open(HISTORY_FILE, "w", encoding="utf-8") as f:
            for record in history:
                f.write(record + "\n")
    except:
        pass  # якщо не вдалося зберегти — не ламаємо програму

def show_history():
    """Показує історію розрахунків"""
    if not history:
        print("Історія порожня.")
    else:
        print("\n=== Історія розрахунків ===")
        for i, record in enumerate(history, 1):
            print(f"{i}. {record}")
        print("===========================\n")

def clear_history():
    """Очищає історію"""
    global history
    history = []
    save_history()
    print("Історія очищена.\n")

def calculator():
    print("=== Консольний Калькулятор v3.0 (з історією) ===\n")
    print("Команди: history - показати історію, clear - очистити історію, exit - вийти\n")
    
    load_history()
    
    while True:
        try:
            a_input = input("Введіть перше число (або 'exit', 'history', 'clear'): ").strip()
            
            if a_input.lower() == 'exit':
                print("Програма завершена. До побачення!")
                save_history()
                break
            elif a_input.lower() == 'history':
                show_history()
                continue
            elif a_input.lower() == 'clear':
                clear_history()
                continue
            
            a = float(a_input)
            
            b_input = input("Введіть друге число: ").strip()
            if b_input.lower() == 'exit':
                print("Програма завершена.")
                save_history()
                break
            b = float(b_input)
            
            action = input("Виберіть дію (+, -, *, /): ").strip()
            
            if action == "+":
                result = a + b
                record = f"{a} + {b} = {result}"
            elif action == "-":
                result = a - b
                record = f"{a} - {b} = {result}"
            elif action == "*":
                result = a * b
                record = f"{a} * {b} = {result}"
            elif action == "/":
                if b == 0:
                    print("Помилка: Ділення на нуль неможливе!\n")
                    continue
                result = a / b
                record = f"{a} / {b} = {result}"
            else:
                print("Помилка: Невідома дія! Використовуйте тільки +, -, *, /\n")
                continue
            
            # Вивід результату
            print(f"Результат: {record}\n")
            
            # Додаємо в історію та зберігаємо
            history.append(record)
            save_history()
            
        except ValueError:
            print("Помилка: Будь ласка, вводьте тільки числа!\n")
        except Exception as e:
            print(f"Невідома помилка: {e}\n")

# Запуск програми
if __name__ == "__main__":
    calculator()
