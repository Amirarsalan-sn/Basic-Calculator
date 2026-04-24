class Calculator:
    def __init__(self):
        pass

    def add(self, num1, num2):
        return num1 + num2

    def substraction(self, num1, num2):
        return num1 - num2

    def multiplication(self, num1, num2):
        return num1 * num2


    def div(self, num1, num2):
        if num2 == 0:
            raise ValueError("what the fuck bro!")
        return num1 / num2
