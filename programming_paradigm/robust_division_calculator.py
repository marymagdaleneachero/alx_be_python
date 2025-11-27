def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)

        divide = num / den
        return f"The result of the division is {divide}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    except ValueError:
        return "Error: Please enter numeric values only."
