from typing import Any, Union

from utils.checking_data_util import is_blocked
from utils.db_util import query_db
from utils.password_util import encrypt_string


def register_account(email, fullname, birth_of_date, sex, username, password, lives_in=None):
    query = "INSERT INTO USER_MESSENGER(email, fullname, birth_of_date, sex, username, password, lives_in)" \
            "VALUES " \
            "('{}','{}',{},'{}','{}','{}')".format(email, fullname, birth_of_date, sex, username,
                                                   password, lives_in)
    if query_db(query):
        return 1
    return 0

def login(username, password):
    if len(username) > 0 and len(password) > 0:
        encrypted_password = encrypt_string(password)
        # Checking user
        query = "SELECT * " \
                "FROM USER_MESSENGER " \
                "WHERE username='{}' and password='{}'".format(username, encrypted_password)

        data_user = query_db(query, is_data_fetched=True)

        if data_user and len(data_user) > 0:
            for data in data_user:
                # Change status login:
                """
                    "status_login":"1 --> user are logging, 0 --> user logout"
                """
                id = data['id']
                query = "UPDATE USER_MESSENGER " \
                        "SET status_login = 1 " \
                        "WHERE " \
                        "id = {}".format(id)

                if query_db(query):
                    print("login successfully")
                    return id
                else:
                    print "Can not login"
        else:
            print 'account does not exist. Please enter 2 to register account'
    else:
        print 'username and password is empty'
    return 0


def logout(user_id):
    query = "UPDATE USER_MESSENGER " \
            "SET status_login = 1 " \
            "WHERE " \
            "id ={};".format(user_id)
    if query_db(query):
        print "logout successfully"
        return 1
    print "Can not login"
    return 0


def search_username(username):
    query = "SELECT id, username\t" \
            "FROM user_messenger\t" \
            "WHERE username like '%{}%'\torder by username ASC ".format(username)

    list_username = query_db(query, is_data_fetched=True)  # type: Union[int, Any]

    if list_username and len(list_username) > 0:
        return list_username
    print "user are not exist. Please try again!"


def block_user(user_id, user_blocked):
    if is_blocked(user_id, user_blocked):
        print "User have been blocked before"

    else:
        print('User does not exist')

    query = "INSERT INTO  blocking_user(user_id, blocked_user_id)\t" \
            "VALUES\t" \
            "({},{})".format(user_id, user_blocked)

    if query_db(query):
        print ('Blocked successfully')
        return 1
    else:
        print('Can not blocked')

    return 0


if __name__ == '__main__':
    register_account("Nguyen Van Tuan", "1988-02-12", "")
