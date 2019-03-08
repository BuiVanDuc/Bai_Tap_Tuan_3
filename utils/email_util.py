# from validate_email import validate_email
# is_valid = validate_email('example@examplecom')
#
# print is_valid

import re

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def is_email_validated(email):
    if EMAIL_REGEX.match(email):
        return True
    else:
        return False

if __name__ == '__main__':
    print is_email_validated('hehe@gmail.com')
