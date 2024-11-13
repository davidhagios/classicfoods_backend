import secrets

def generate_secret_key():
    return secrets.token_urlsafe(100)

print(generate_secret_key())