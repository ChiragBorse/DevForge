"""
DevForge - Password Generator

Generates random passwords using letters,
numbers, and special characters.
"""

import secrets
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main():
    print("=== DevForge Password Generator ===")

    try:
        length = int(input("Enter password length (8-64): "))

        if length < 8 or length > 64:
            print("Error: Password length must be between 8 and 64.")
            return

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

    except ValueError:
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    main()
