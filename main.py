import sys
import random

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QInputDialog, QMessageBox
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Калькулятор Моделі А412ОМ")
        self.setFixedSize(600, 400)
        self.init_ui()

    def init_ui(self):
        title = QLabel("Калькулятор Моделі А412ОМ")
        title.setFont(QFont("Courier New", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        desc = QLabel("Рахуй Числа!")
        desc.setFont(QFont("Courier New", 18))
        desc.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btn_calc = QPushButton("Звичайні Обчислення")
        btn_calc.clicked.connect(self.normal_calculator)

        btn_task = QPushButton("Випадкова Задача")
        btn_task.clicked.connect(self.math_trainer)

        btn_guess = QPushButton("Вгадай Число")
        btn_guess.clicked.connect(self.guess_game)

        btn_exit = QPushButton("Виключити Программу")
        btn_exit.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(title)
        vbox.addWidget(desc)
        vbox.addSpacing(30)
        vbox.addWidget(btn_calc)
        vbox.addWidget(btn_task)
        vbox.addWidget(btn_guess)
        vbox.addWidget(btn_exit)
        vbox.addStretch()
        self.setLayout(vbox)

    def normal_calculator(self):
        expr, ok = QInputDialog.getText(self, "Звичайний калькулятор", "Введіть вираз:")
        if ok and expr:
            try:
                result = eval(expr, {"__builtins__": None}, {})
                QMessageBox.information(self, "Результат", f"Результат: {result}")
            except ZeroDivisionError:
                QMessageBox.warning(self, "Помилка", "Помилка ділення!")
            except Exception as e:
                QMessageBox.warning(self, "Помилка", f"Помилка: {type(e).__name__}")

    def generate_problem(self):
        a = random.randint(1, 20)
        b = random.randint(1, 20)
        op = random.choice(["+", "-", "*", "/"])
        if op == "/":
            b = random.randint(1, 20)
        problem = f"{a} {op} {b}"
        answer = eval(problem)
        if isinstance(answer, float):
            answer = round(answer, 2)
        return problem, answer

    def math_trainer(self):
        problem, correct_answer = self.generate_problem()
        user_input, ok = QInputDialog.getText(self, "Тренування", f"Розв'яжіть: {problem}")
        if ok and user_input:
            try:
                user_answer = float(user_input)
                if abs(user_answer - float(correct_answer)) < 0.01:
                    QMessageBox.information(self, "Результат", "Правильно!")
                else:
                    QMessageBox.information(self, "Результат", f"Невірно. Правильна відповідь: {correct_answer}")
            except Exception:
                QMessageBox.warning(self, "Помилка", "Вводьте тільки числа!")

    def guess_game(self):
        secret = random.randint(1, 50)
        attempts = 0
        while True:
            guess, ok = QInputDialog.getInt(
                self, "Вгадай Число", "Я загадав число від 1 до 50. Спробуй вгадати!",
                min=1, max=50
            )
            if not ok:
                break
            attempts += 1
            if guess < secret:
                QMessageBox.information(self, "Підказка", "Моє число більше!")
            elif guess > secret:
                QMessageBox.information(self, "Підказка", "Моє число менше!")
            else:
                QMessageBox.information(self, "Вітаю!", f"Победа! Угадав за {attempts} спроб!")
                break

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec())
