def secret_message(message):
    """
    This function takes a string and returns a secret message
    by replacing characters with numbers and separating them with hyphens.
    """
    secret = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                secret += str(ord(char) - ord('a') + 1) + '-'
            else:
                secret += str(ord(char) - ord('A') + 1) + '-'
        elif char == " ":
            if secret.endswith('-'):
                secret = secret[:-1]
            secret += ' '

    # Remove any trailing hyphen at the end of the string
    if secret.endswith('-'):
        secret = secret[:-1]

    return secret

# Example usage:
message = input()
secret = secret_message(message)
print(secret)
