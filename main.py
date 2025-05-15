import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_specials:
        chars += string.punctuation

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("Random Password Generator")
    length = int(input("Enter password length: "))
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_specials = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_digits, use_specials)
    print(f"Generated password: {password}")
