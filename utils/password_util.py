import re
import hashlib
import bcrypt


def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature

def validate_password(password):
    if len(password) < 8:
        print("Make sure your password is at lest 8 letters")
    else:
        if re.search('[0-9]', password) is None:
            print("Make sure your password has a number in it")
            return 0
        elif re.search('[A-Z]', password) is None:
            print("Make sure your password has a capital letter in it")
            return 0
        elif re.search('[!@#$%^*_=]', password) is None:
            print("Make sure your password has a special character in it")
            return 0
        return 1
    print ('password is valid')
    return 0

if __name__ == '__main__':
    print encrypt_string('abc')


