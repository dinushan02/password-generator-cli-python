import random
import string

# Optional clipboard support
try:
    import pyperclip
    CLIPBOARD_AVAILABLE = True
except ImportError:
    CLIPBOARD_AVAILABLE = False


def get_user_choices():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Enter a valid positive number!")
            return None

        use_upper = input("Include uppercase? (y/n): ").lower()
        use_numbers = input("Include numbers? (y/n): ").lower()
        use_symbols = input("Include symbols? (y/n): ").lower()

        if use_upper not in ["y", "n"] or use_numbers not in ["y", "n"] or use_symbols not in ["y", "n"]:
            print("Please enter y or n for all options!")
            return None

        return length, use_upper, use_numbers, use_symbols

    except ValueError:
        print("Please enter a valid number!")
        return None


def generate_password(length, use_upper, use_numbers, use_symbols):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    all_chars = lowercase
    password = []

    # Ensure at least one of each selected type
    if use_upper == "y":
        password.append(random.choice(uppercase))
        all_chars += uppercase

    if use_numbers == "y":
        password.append(random.choice(digits))
        all_chars += digits

    if use_symbols == "y":
        password.append(random.choice(symbols))
        all_chars += symbols

    # Fill remaining
    while len(password) < length:
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return "".join(password)


def main():
    print("Welcome to Password Generator")

    while True:
        data = get_user_choices()

        if data:
            length, use_upper, use_numbers, use_symbols = data
            password = generate_password(length, use_upper, use_numbers, use_symbols)

            print(f"\nGenerated Password: {password}")

            if CLIPBOARD_AVAILABLE:
                pyperclip.copy(password)
                print("Password copied to clipboard!")

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != "y":
            print("Goodbye 👋")
            break


if __name__ == "__main__":
    main()
    
    
    
    