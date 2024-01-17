class Expression:
    def accept(self, visitor):
        pass


class Literal(Expression):
    def __init__(self, value):
        self.value = value

    def accept(self, visitor):
        return visitor.visit_literal(self)


class BinaryOperation(Expression):
    def __init__(self, left, right, sign):
        self.left = left
        self.right = right
        self.sign = sign

    def accept(self, visitor):
        return visitor.visit_binary_operation(self)


class Brackets(Expression):
    def __init__(self, inner_expression):
        self.inner_expression = inner_expression

    def accept(self, visitor):
        return visitor.visit_brackets(self)


class Visitor:
    def visit_literal(self, expression):
        pass

    def visit_binary_operation(self, expression):
        pass

    def visit_brackets(self, expression):
        pass


class PrintExpression(Visitor):
    def __init__(self):
        self.srt = ""

    def visit_literal(self, expression):
        self.srt += str(expression.value)

    def visit_binary_operation(self, expression):
        expression.left.accept(self)
        self.srt += f" {expression.sign} "
        expression.right.accept(self)

    def visit_brackets(self, expression):
        self.srt += "("
        expression.inner_expression.accept(self)
        self.srt += ")"


def main():
    expression = BinaryOperation(BinaryOperation(Literal(1), Literal(2), "+"), Literal(3), "+")
    print_expression = PrintExpression()
    expression.accept(print_expression)
    print(f"Результат: {print_expression.srt}")

    more_expression = BinaryOperation(Literal(3), Brackets(BinaryOperation(Literal(1), Literal(2), "+")), "*")
    more_print_expression = PrintExpression()
    more_expression.accept(more_print_expression)
    print(f"Результат: {more_print_expression.srt}")


if __name__ == "__main__":
    main()
