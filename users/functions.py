from utils.db_utils.db_collection import query_db
from utils.db_utils.query_user import QUERY_REGISTER_ACCOUNT, QUERY_LOGIN, QUERY_STATUS_LOGIN, QUERY_LOGOUT, \
    QUERY_SEARCH_USERNAME, QUERY_BLOCKED_USER, QUERY_LIST_BLOCK, QUERY_UNBLOCK_USER, QUERY_EMAIL, QUERY_UNBLOCK, \
    QUERY_USER_BLOCKED, QUERY_INFO_BY_ID


def register(email, fullname, birth_of_date, sex, username, password, lives_in=None):
    if query_db(QUERY_REGISTER_ACCOUNT, (email, fullname, birth_of_date, sex, username, password, lives_in,)):
        return True
    return False


def login(username, password):
    list_data = query_db(QUERY_LOGIN, (username, password,), is_data_fetched=True)

    if list_data and len(list_data) > 0:
        user_id = list_data[0]['id']
        if change_status_login(user_id):
            print("login successfully")
            return True
        else:
            print "Can not login"
    return False


def logout(user_id):
    if query_db(QUERY_LOGOUT, (user_id)):
        print "logout successfully"
        return True
    print "(Waring) Can not logout"
    return False


def search_username(username):
    list_username = query_db(QUERY_SEARCH_USERNAME, ("%" + username + "%",), is_data_fetched=True)
    return list_username


def is_blocked(user_id, user_id_blocked):
    # inform data1 user blocked a other user
    list_data_1 = query_db(QUERY_USER_BLOCKED, (user_id, user_id_blocked), is_data_fetched=True)
    # inform data2 user were blocked by a other user
    list_data_2 = query_db(QUERY_USER_BLOCKED, (user_id_blocked, user_id), is_data_fetched=True)

    if list_data_1 and len(list_data_1) > 0:
        return 1
    elif list_data_2 and len(list_data_2) > 0:
        return 2

    return 0


def block(user_id, user_id_blocked):
    if query_db(QUERY_BLOCKED_USER, (user_id, user_id_blocked,)):
        return True
    else:
        print('Can not blocked')

    return False


def show_list_block(user_id):
    # Show list block
    list_block = query_db(QUERY_LIST_BLOCK, (user_id,), is_data_fetched=True)

    if list_block and len(list_block) > 0:
        return list_block


def unblock(user_id):
    if query_db(QUERY_UNBLOCK_USER, (user_id), is_data_fetched=True):
        print "Unblock successfully"
        return True

    print "Can not unblock"
    return False


def is_email_existed(email):
    list_data = query_db(QUERY_EMAIL, (email,), is_data_fetched=True)

    if list_data and len(list_data) > 0:
        return True
    return False


def change_status_login(id):
    if query_db(QUERY_STATUS_LOGIN, (id,)):
        return True
    return False


def get_id(username, password):
    list_data = query_db(QUERY_LOGIN, (username, password,), is_data_fetched=True)
    user_id = list_data[0]['id']
    return user_id


def get_user_info_by_id(user_id):
    ret_data = query_db(QUERY_INFO_BY_ID, (user_id,), is_data_fetched=True)

    if ret_data and len(ret_data) > 0:
        item = ret_data[0]
        return item


def remove_block(user_id, user_id_blocked):
    if query_db(QUERY_UNBLOCK, (user_id, user_id_blocked)):
        return True
    return False


def view_list_block(user_id):
    list_users_blocked = query_db(QUERY_LIST_BLOCK, (user_id,), is_data_fetched=True)

    return list_users_blocked
