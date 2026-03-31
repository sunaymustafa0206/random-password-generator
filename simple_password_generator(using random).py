import random
import string

def generate_password(length=12):
    # Combine all characters: uppercase, lowercase, digits, and punctuation
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the pool
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

# Example usage:
print("Your password is:", generate_password(16))
