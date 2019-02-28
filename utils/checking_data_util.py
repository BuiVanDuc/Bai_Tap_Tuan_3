from utils.db_util import query_db


def is_existed_user(user_id, is_fetching_data=False):
    query = "SELECT * FROM USER_MESSENGER " \
            "WHERE id ={}".format(user_id)
    if is_fetching_data:
        return query_db(query, is_fetching_data=True)
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
