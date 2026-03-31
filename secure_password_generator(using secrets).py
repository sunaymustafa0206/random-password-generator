import secrets
import string

def generate_secure_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    # Use secrets.choice for higher security
    password = ''.join(secrets.choice(alphabet) for _ in range(length))
    return password

print("Secure password:", generate_secure_password())
