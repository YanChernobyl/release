import random 

def show_menu():
    print("\n*** Калькулятор Моделі А412ОМ ***")
    print("1. Звичайні Обчислення (+-*/)")
    print("2. Випадкова Задача")
    print("3. Вгадай Число")
    print("4. Виключити Программу")

def normal_calculator():
    print("\n[Звичайний режим] Введіть вираз:")

    try:
        expr = input(">>> ").strip()
        result = eval(expr)
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Некоректне Введення")

def generate_problem():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ops = ["+", "-", "*", "/"]
    op = random.choice(ops)

    #1
    if op == "/" and b == 0:
        b = 1 #На всякий случай на костылях

    problem = f"{a} {op} {b}"
    answer = eval(problem)
    return problem, round(answer, 2) if isinstance(answer, float) else answer

def math_trainer():
    print("\n[Тренування] Розв'яжіть завдання:")
    problem, correct_answer = generate_problem()