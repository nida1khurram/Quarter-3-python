class Calculator:
    def add(self, a: float, b: float) -> float:
        """Adds two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtracts the second number from the first."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplies two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Divides the first number by the second. Raises ValueError if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
