def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("===================================")
    print("Hello from GitHub Actions CI/CD!")
    print("This print is coming from app.py")
    print("===================================")

    print("Simple Calculator Results:")
    print("2 + 3 =", add(2, 3))
    print("10 - 4 =", subtract(10, 4))
    print("5 * 6 =", multiply(5, 6))
    print("20 / 4 =", divide(20, 4))