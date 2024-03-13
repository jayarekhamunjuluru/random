import string
import secrets

def generate_password(length=12):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter the length of the password: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)16