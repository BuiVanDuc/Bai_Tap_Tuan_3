from utils.db_utils.db_collection import query_db
from utils.db_utils.query_friend import QUERY_FRIENDS_IN_MESSAGE, QUERY_FRIENDS, \
    QUERY_ADD_FRIEND, \
    QUERY_DETAIL_FRIEND, QUERY_GROUP_FRIENDS, QUERY_SEARCHING_FRIEND, QUERY_EDIT_NICKNAME, QUERY_FRIEND, QUERY_UNFRIEND, \
    QUERY_FRIEND_BLOCK


# Optimal code
def view_friends_by_contact_time(user_id):
    # Query friend in message
    list_friends_in_message = query_db(QUERY_FRIENDS_IN_MESSAGE, (user_id,), is_data_fetched=True)
    list_friend_ids = list()
    list_friends = list()

    if len(list_friends_in_message) > 0:
        for friend in list_friends_in_message:
            if friend['friend_id'] not in list_friend_ids:
                list_friend_ids.append(friend['friend_id'])
                list_friends.append(friend)

    if len(list_friend_ids) > 0:
        # have no any friend in message:
        list_friends_not_in_message = query_db(QUERY_FRIENDS, (user_id,), is_data_fetched=True)
        if len(list_friends_not_in_message) > 0:
            for friend in list_friends_not_in_message:
                if friend['friend_id'] not in list_friend_ids:
                    list_friends.append(friend)

    return list_friends


def view_friends(user_id):
    list_friends = query_db(QUERY_FRIENDS, (user_id,), is_data_fetched=True)
    if list_friends and len(list_friends) > 0:
        return list_friends


def add_friend(user_id, friend_id, username):
    if query_db(QUERY_ADD_FRIEND, (user_id, friend_id, username)):
        return True
    return False


def detail_friend(friend_id):
    list_info_friend = query_db(QUERY_DETAIL_FRIEND, (friend_id,), is_data_fetched=True)

    return list_info_friend


def group_friend_by_lives_in(user_id):
    list_friends = query_db(QUERY_GROUP_FRIENDS, (user_id,), is_data_fetched=True)
    ret_data = dict()

    for friend in list_friends:
        lives_in = friend['lives_in'].lower()

        if lives_in in ret_data:
            ret_data[lives_in].append(friend['nickname'])
        else:
            ret_data[lives_in] = list()
            ret_data[lives_in].append(friend['nickname'])

    return ret_data


def search_friend(user_id, nickname):
    list_friends = query_db(QUERY_SEARCHING_FRIEND, (user_id, '%' + nickname + '%',), is_data_fetched=True)

    return list_friends


def edit_nicknames(friend_id, new_nickname):
    if query_db(QUERY_EDIT_NICKNAME, (new_nickname, friend_id)):
        print " edit successfully"
        return 1
    print "edit unsuccessfully"
    return 0


def is_friend_existed(user_id, friend_id):
    list_data = query_db(QUERY_FRIEND, (user_id, friend_id,), is_data_fetched=True)

    if list_data and len(list_data) > 0:
        return True
    return False


def remove_friend(user_id, friend_id):
    if query_db(QUERY_UNFRIEND, (user_id, friend_id)):
        return True
    return False


def list_friend_blocked(user_id):
    return list_friend_blocked == query_db(QUERY_FRIEND_BLOCK, (user_id,), is_data_fetched=True)