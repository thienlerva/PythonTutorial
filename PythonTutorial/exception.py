
# x = input("Enter number 1: ")
# y = input("Enter second number: ")
# try:
#     z = int(x) / int(y)
#     print(f"Division is: {z}")
# except ZeroDivisionError as e:
#     print(f"Exception: {e}")
# except TypeError as e:
#     print(f"Exception: {e}")
# except Exception as e:
#     print(f"Excetion type: {e}")

# User-defined exception
# class Accident(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#
#     def print_exception(self):
#         print(f"User defined exception: {self.msg}")
#
# try:
#     raise Accident('Crash between two cars')
# except Accident as e:
#     e.print_exception()

# finally clause
def process_file():
    global f
    try:
        f = open("data.txt")
        x = 1/0
    except FileNotFoundError as e:
        print(f"Exception {e}")
    except ZeroDivisionError as e:
        print(f"Exception {e}")
    finally:
        print("Cleaning up file")
        f.close()

process_file()