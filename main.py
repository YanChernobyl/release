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
    print(problem)

    try:
        user_answer = float(input("Ваша Відповідь: "))
        if abs(user_answer - correct_answer) < 0.01:
            print("Правильньно!")
        else:
            print(f"Невірно. Правильна відповідь: {correct_answer}")
    except:
        print("Вводите только числа!")

def guess_game():
    print("\n Я загадав число від 1 до 50. спробуй вгадать!")
    secret = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Твоя догадка: "))
            attempts += 1 

            if guess < secret:
                print("Моє число більше!")
            elif guess > secret:
                print("Моє число менше!")
            else:
                print(f"Победа! Угадав за {attempts} попиток!")
                break
        except:
            print("Вводи ціли числа!")
            continue

def main():
    print("Привіт! Це не просто калькулятор.")

    while True:
        show_menu()
        choice = input("Вибери Дію (1-4): ")

        if choice == "1":
            normal_calculator()
        elif choice == "2":
            math_trainer()
        elif choice == "3":
            guess_game()
        elif choice == "4":
            print("До Побачення!")
            break
        else:
            print("Незрозумілий вибір. Спробуй ще раз")

if __name__ == "__name__":
    main()