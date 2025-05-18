import sys
import random

from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout,
    QInputDialog, QMessageBox, QLineEdit
)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class ButtonCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кнопковий калькулятор")
        self.setFixedSize(350, 400)
        self.calc_expression = ''
        self.init_ui()

    def init_ui(self):
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAignment(Qt.AlignmentFlag.AlignRight)
        self.display.setFont(QFont("Arial", 24))

        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]

        grid_layout = QVBoxLayout()
        for row in buttons:
            h_box = QHBoxLayout()
            for btn_text in row:
            QPushButton(btn_text)
                button.setFixedSize(60, 60)
                button.clicked.connect(self.on_button_click)
                h_box.addWidget(button)
            grid_layout.addLayout(h_box)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.display)
        main_layout.addLayout(grid_layout)
        slf.setLayout(main_layout)

    def on_button_click(self):
        text = self.sender().text()
        if text == '=':
            try:
                result = str(eval(self.calc_expression))
                self.display.setText(result)
                self.calc_expression = result
            except:
                self.display.setText("Помилка")
                self.calc_expression = ''
        else:
            self.calc_expression += text
            self.display.setText(self.calc_expression)

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

        btn_buttons_calc = QPushButton("Калькулятор з кнопками")
        btn_buttons_calc.clicked.connect(self.open_button_calculator)

        btn_exit = QPushButton("Виключити Программу")
        btn_exit.clicked.connect(self.close)

        vbox = QVBoxLayout()
        vbox.addWidget(title)
        vbox.addWidget(desc)
        vbox.addSpacing(30)
        vbox.addWidget(btn_calc)
        vbox.addWidget(btn_task)
        vbox.addWidget(btn_guess)
        vbox.addWidget(btn_buttons_calc)
        vbox.addWidget(btn_exit)
        vbox.addStretch()
        self.setLayout(vbox)

    def open_button_calculator(self):
        self.button_calc_window = ButtonCalculator()
        self.button_calc_window.show()
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
