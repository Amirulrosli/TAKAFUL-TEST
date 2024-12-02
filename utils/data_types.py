class Money(float):
    def __new__(cls, value):
        if value < 0:
            raise ValueError("Money cannot be negative.")
        return super().__new__(cls, value)

class InterestRate(float):
    def __new__(cls, value):
        if not 0 <= value <= 1:
            raise ValueError("Interest rate must be between 0 and 1.")
        return super().__new__(cls, value)

class Period(int):
    def __new__(cls, value):
        if value <= 0:
            raise ValueError("Period must be positive.")
        return super().__new__(cls, value)