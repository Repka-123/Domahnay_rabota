import operator
import math

class MiniLangInterpreter:
    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '%': operator.mod,
            '^': operator.pow,
        }

    def evaluate_expression(self, expression: str) -> float:
        tokens = self.tokenize(expression)
        postfix = self.to_postfix(tokens)
        return self.calculate(postfix)

    def tokenize(self, expression: str):
        # Преобразует строку в список токенов (числа и операторы)
        tokens = []
        num = ""
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            elif char in self.operators:
                if num:
                    tokens.append(float(num))
                    num = ""
                tokens.append(char)
            elif char == ' ' and num:
                tokens.append(float(num))
                num = ""
        if num:
            tokens.append(float(num))
        return tokens

    def to_postfix(self, tokens):
        # Преобразует инфиксное выражение в постфиксное
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2, '^': 3}
        output = []
        stack = []
        for token in tokens:
            if isinstance(token, (int, float)):
                output.append(token)
            elif token in self.operators:
                while stack and precedence.get(stack[-1], 0) >= precedence[token]:
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def calculate(self, postfix):
        # Вычисляет значение постфиксного выражения
        stack = []
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            elif token in self.operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(self.operators[token](a, b))
        return stack[0]


# Пример использования
if __name__ == "__main__":
    interpreter = MiniLangInterpreter()
    expression = "3 + 5 * 2 - 8 / 4 ^ 2"
    result = interpreter.evaluate_expression(expression)
    print(f"Result of '{expression}': {result}")
