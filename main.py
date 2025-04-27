import pygame
import random

def start_screen():
    pygame.init()

    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Екран Опису")

    # Кольори
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    BLUE = (0, 31, 102)
    HOVER_BLUE = (0, 54, 177)

    # Шрифти
    title_font = pygame.font.SysFont("Courier New", 48)
    desc_font = pygame.font.SysFont("Courier New", 32)
    button_font = pygame.font.SysFont("Courier New", 36)

    # Тексти
    title_text = title_font.render("Калькулятор Моделі А412ОМ", True, WHITE)
    desc_text = desc_font.render("Рахуй Числа!", True, WHITE)
    button_text = button_font.render("Почати", True, WHITE)

    # Кнопка
    button_rect = pygame.Rect(WIDTH // 2 - 100, 400, 200, 60)

    first_screen = True
    while first_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    first_screen = False  # Перехід до гри

        screen.fill(BLACK)

        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))
        screen.blit(desc_text, (WIDTH // 2 - desc_text.get_width() // 2, 250))

        mouse_pos = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, HOVER_BLUE, button_rect)
        else:
            pygame.draw.rect(screen, BLUE, button_rect)

        screen.blit(button_text, (button_rect.centerx - button_text.get_width() // 2,
                                   button_rect.centery - button_text.get_height() // 2))

        pygame.display.flip()

    pygame.quit()  # Закриваємо pygame перед запуском консольного калькулятора

def show_menu():
    print("\n*** Калькулятор Моделі А412ОМ ***")
    print("1. Звичайні Обчислення (+-*/)")
    print("2. Випадкова Задача")
    print("3. Вгадай Число")
    print("4. Виключити Програму")

def normal_calculator():
    print("\n[Звичайний режим] Введіть вираз:")

    try:
        expr = input(">>> ").strip()
        result = eval(expr)
        print(f"Результат: {result}")
    except ZeroDivisionError:
        print("Помилка ділення на нуль!")
    except Exception as e:
        print(f"Помилка: {type(e).__name__}")

def generate_problem():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    ops = ["+", "-", "*", "/"]
    op = random.choice(ops)

    if op == "/" and b == 0:
        b = 1  # запобігти діленню на нуль

    problem = f"{a} {op} {b}"
    answer = eval(problem)
    return problem, round(answer, 2) if isinstance(answer, float) else answer

def math_trainer():
    print("\n[Тренування] Розв'яжіть завдання:")
    problem, correct_answer = generate_problem()
    print(problem)

    try:
        user_answer = float(input("Ваша відповідь: "))
        if abs(user_answer - correct_answer) < 0.01:
            print("Правильно!")
        else:
            print(f"Невірно. Правильна відповідь: {correct_answer}")
    except ValueError:
        print("Введіть тільки числа!")

def guess_game():
    print("\nЯ загадав число від 1 до 50. Спробуй вгадати!")
    secret = random.randint(1, 50)
    attempts = 0

    while True:
        try:
            guess = int(input("Твоя спроба: "))
            attempts += 1

            if guess < secret:
                print("Моє число більше!")
            elif guess > secret:
                print("Моє число менше!")
            else:
                print(f"Перемога! Вгадав за {attempts} спроб!")
                break
        except ValueError:
            print("Вводьте тільки цілі числа!")

def main():
    print("Привіт! Це не просто калькулятор.")

    while True:
        show_menu()
        choice = input("Виберіть дію (1-4): ")

        if choice == "1":
            normal_calculator()
        elif choice == "2":
            math_trainer()
        elif choice == "3":
            guess_game()
        elif choice == "4":
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")


start_screen()  # Показати екран опису
main()          # Запустити головне консольне меню
