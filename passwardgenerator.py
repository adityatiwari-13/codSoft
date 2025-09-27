import random
import string

def password_generator():
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Length should be a positive integer.")
            return
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"Generated Password: {password}")
password_generator()
