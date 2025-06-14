#! theres a bug when the hypotenuse is known the program does not calculate the other side

import sys

def pythagorean_theorem(a, b):
    # Calculate the length of the hypotenuse of a right triangle given the lengths of the other two sides.
    return (a**2 + b**2) ** 0.5

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python pythagorean_theorem.py <side_a> <side_b>")
        sys.exit(1)

    try:
        side_a = float(sys.argv[1])
        side_b = float(sys.argv[2])
    except ValueError:
        print("Both sides must be numbers.")
        sys.exit(1)

    hypotenuse = pythagorean_theorem(side_a, side_b)
    print(f"The length of the hypotenuse is: {hypotenuse}")
    print(f"Or the the square root of: {hypotenuse**2:.0f}")