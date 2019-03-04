from utils.db_util import query_db


def is_existed_user(user_id, is_data_fetched=False):
    query = "SELECT * FROM user_messenger\t" \
            "WHERE id ={}".format(user_id)
    if is_data_fetched:
        return query_db(query, is_data_fetched=True)
    if query_db(query):
        return True
    return False


def is_blocked(user_id, user_blocked):
    query = "SELECT * " \
            "FROM blocking_user " \
            "WHERE user_id ={} and blocked_user_id={}".format(user_id, user_blocked)
    if query_db(query):
        return True
    return False


def is_existed_friend(user_id, friend_id):
    query = "SELECT * " \
            "FROM USER_FRIEND " \
            "WHERE user_id={} and friend_id={}".format(user_id, friend_id)
    if query_db(query):
        return 1
    return 0


def is_email_existed(email):
    query = "SELECT *\t" \
            "FROM user_messenger\t" \
            "WHERE email like '{}'".format(email)

    if query_db(query):
        return 1
    return 0


def update_status_user_login(user_id):
    query = "UPDATE USER_MESSENGER " \
            "SET status_login = 1 " \
            "WHERE\t" \
            "id = {}".format(user_id)

    if query_db(query):
        return 1
    return 0

if __name__ == '__main__':
    is_blocked(1,4)