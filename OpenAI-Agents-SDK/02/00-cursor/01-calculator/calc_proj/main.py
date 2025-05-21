from Calculator import Calculator

# Create an instance of the Calculator class
calculator = Calculator()

# Perform some calculations
sum_result = calculator.add(10.5, 5.2)
difference_result = calculator.subtract(20, 7)
product_result = calculator.multiply(4, 6.5)

try:
    division_result = calculator.divide(100, 5)
    division_by_zero_result = calculator.divide(10, 0) # This will raise an error
except ValueError as e:
    division_by_zero_error = str(e)

# Print the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")
print(f"Division by zero error: {division_by_zero_error}")
