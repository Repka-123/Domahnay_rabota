import pytest
from main import MiniLangInterpreter

@pytest.mark.parametrize(
    "expression, expected_result",
    [
        ("3 + 5", 8),                   # Простое сложение
        ("10 - 3", 7),                  # Простое вычитание
        ("4 * 2", 8),                   # Умножение
        ("8 / 2", 4),                   # Деление
        ("10 % 3", 1),                  # Остаток от деления
        ("2 ^ 3", 8),                   # Возведение в степень
        ("3 + 5 * 2", 13),              # Приоритет операторов
        ("10 - 4 / 2", 8),              # Приоритет операторов с вычитанием и делением
        ("10 - (4 / 2)", 8),            # Скобки
        ("(3 + 5) * 2", 16),            # Скобки изменяют приоритет
        ("4 * 3 / 6", 2),               # Умножение и деление
        ("4 + 3 * 2 - 7 / 1", 7),       # Комплексное выражение
    ]
)
def test_interpreter(expression, expected_result):
    interpreter = MiniLangInterpreter()
    result = interpreter.evaluate_expression(expression)
    assert math.isclose(result, expected_result, rel_tol=1e-9), f"Failed for: {expression}"
