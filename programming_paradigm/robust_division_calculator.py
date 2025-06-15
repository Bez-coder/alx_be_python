def safe_divide(numerator, denominator):
    """Performs safe division while handling errors."""
    try:
        num = float(numerator)
        denom = float(denominator)

        if denom == 0:
            return "Error: Cannot divide by zero."

        return f"The result of the division is {num / denom:.2f}"

    except ValueError:
        return "Error: Please enter numeric values only."
import sys
from robust_division_calculator import safe_divide

def main():
    """Handles command-line interaction for safe division."""
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)

    numerator = sys.argv[1]
    denominator = sys.argv[2]

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
