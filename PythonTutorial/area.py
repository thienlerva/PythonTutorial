
def calculate_area(base, height):
    print("__name__: ", __name__)
    return 1/2 * (base * height)

if __name__ == "__main__":  # this is the main program
    print("I am in area.py")
    a = calculate_area(10, 20)
    print(f"Area: {a}")