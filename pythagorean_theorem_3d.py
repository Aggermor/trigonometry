import sys
from pythagorean_theorem import pythagorean_theorem

def pythagorean_theorem_3d(a, b, c):
    # Calculate the length of the crosssectional hypotenuse using the Pythagorean theorem of a 3-dimensional right triangle
    # Hypotenuse = sqrt(a^2 + b^2)
    # a = length of the bottom side, left to right
    # b = length of the bottom side, front to back
    # c = length of the vertical side, bottom to top
    # for now, the hight argument must be the vertical side
    
    hypotenuse = pythagorean_theorem(a, b)
    return (hypotenuse**2 + c**2)**0.5

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pythagorean_theorem.py <side_a> <side_b> <side_c>")
        sys.exit(1)

    try:
        side_a = float(sys.argv[1])
        side_b = float(sys.argv[2])
        side_c = float(sys.argv[3])
    except ValueError:
        print("All sides must be numbers.")
        sys.exit(1)

    hypotenuse = pythagorean_theorem(side_a, side_b)
    hypotenuse_3d = pythagorean_theorem_3d(side_a, side_b, side_c)
    print(f"The length of the 3D hypotenuse is: {hypotenuse_3d}")
    print(f"Or the the square root of: {hypotenuse_3d**2:.0f}")