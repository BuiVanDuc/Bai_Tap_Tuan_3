import hashlib
import re


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def validate_password(password):
    warning = "For your account security, your new password must:\n" \
              "+ Contain at least 8 characters\n" \
              "+ Contain any combination of letters, digits, and special characters"
    if len(password) < 8:
        print(warning)
    elif re.search('[a-zA-Z0-9]', password) is None:
        print(warning)
    elif re.search('[!@#$%^*_=]', password) is None:
        print(warning)
    else:
        return 1

    return 0

if __name__ == '__main__':
    print encrypt_string('abc')


