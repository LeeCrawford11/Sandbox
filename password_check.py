"""
Lee Crawford
CP1404
Password Check
"""

def main():
    minimum_length = 4
    password = input("Enter your password:")
    while not len(password) >= minimum_length:
        print(f"Password must be {minimum_length} or more characters")
        password = input("Enter your password:")
    print("*" * (len(password)))


main()