def circle_area(radius):
    pi = 3.14159
    area = pi * radius ** 2
    return area


def calculate_tax(money, tax):
    total_due = money + (money * tax)
    return total_due


def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius


# Circle
radius = float(input())
print(f"{circle_area(radius):.2f}")

# Taxes
money = float(input())
tax = float(input())
print(f"{calculate_tax(money, tax):.2f}")

# Temperature
fahrenheit = float(input())
print(fahrenheit_to_celsius(fahrenheit))