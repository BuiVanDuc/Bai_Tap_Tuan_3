from utils.checking_data_util import is_existed_friend, is_existed_user, is_blocked
from utils.db_util import query_db


def show_list_friends(user_id):
    # Query friend in message
    query = "SELECT user_friend.friend_id, user_friend.nickname\t" \
            "FROM user_friend\t" \
            "INNER JOIN MESSAGE\t" \
            "ON message.sender_id = user_friend.friend_id or message.recipient_id=user_friend.friend_id\t" \
            "WHERE user_friend.user_id ={} ORDER BY message.delivered_time DESC".format(user_id)

    list_friends_in_message = query_db(query, is_data_fetched=True)
    list_friend_ids = list()
    list_friends = list()

    if len(list_friends_in_message) > 0:
        for friend in list_friends_in_message:
            if friend['friend_id'] not in list_friend_ids:
                list_friend_ids.append(friend['friend_id'])
                list_friends.append(friend)

    if len(list_friend_ids) > 0:
        # Query friend not in message
        query = "SELECT friend_id, nickname\t" \
                "FROM USER_FRIEND\t" \
                "WHERE friend_id NOT IN {}".format(tuple(list_friend_ids))

        list_friends_not_in_message = query_db(query, is_data_fetched=True)
        if len(list_friends_not_in_message) > 0:
            for friend in list_friends_not_in_message: list_friends.append(friend)
    else:
        # have no any friend in message:
        query= "SELECT friend_id, nickname\t" \
                "FROM USER_FRIEND\t" \
                "WHERE user_id ={}\torder by nickname DESC".format(tuple(user_id))

        list_friends_not_in_message = query_db(query, is_data_fetched=True)
        if len(list_friends_not_in_message) > 0:
            for friend in list_friends_not_in_message: list_friends.append(friend)

    return list_friends


def add_friend(friend_id, user_id):
    data = is_existed_user(friend_id, is_data_fetched=True)
    if data and len(data) > 0:
        nickname = data[0]['username']
        if is_existed_user(friend_id):
            if is_existed_friend(user_id, friend_id):
                print "Friend is existing"
                return 1
            query = "INSERT INTO USER_FRIEND(user_id, friend_id, nickname)\t" \
                    "VALUES " \
                    "({},{},'{}')".format(user_id, friend_id, nickname)

            adding_result = query_db(query)

            if adding_result:
                print('add friend successfully')
                return 1
            else:
                print "user have been a friend"
        else:
            print "Can not add friend"
    else:
        print('User friend is not exist')
    return 0

def edit_nicknames(friend_id, new_nickname):
    query = "UPDATE user_friend\t" \
            "SET nickname='{}'\tWHERE friend_id={}".format(new_nickname, friend_id)

    if query_db(query):
        print " edit successfully"
        return 1
    print "edit unsuccessfully"
    return 0


def detail_friend(friend_id):
    query = "SELECT USER_MESSENGER.fullname, USER_MESSENGER.sex, USER_MESSENGER.birth_of_date, USER_MESSENGER.username, USER_MESSENGER.lives_in\t" \
            "FROM USER_MESSENGER\t" \
            "WHERE USER_MESSENGER.id={}".format(friend_id)

    list_info_friend = query_db(query, is_data_fetched=True)

    return list_info_friend

def group_friend_by_lives_in(user_id):
    query = "SELECT user_friend.friend_id,  user_friend.nickname, user_messenger.lives_in " \
            "FROM user_friend " \
            "INNER JOIN user_messenger " \
            "ON user_friend.friend_id = user_messenger.id " \
            "WHERE user_friend.user_id = {} ORDER BY user_messenger.lives_in ASC".format(user_id)

    list_friends = query_db(query, is_data_fetched=True)
    ret_data = dict()

    for friend in list_friends:
        lives_in = friend['lives_in'].lower()

        if lives_in in ret_data:
            ret_data[lives_in].append(friend['nickname'])
        else:
            ret_data[lives_in] = list()
            ret_data[lives_in].append(friend['nickname'])

    return ret_data


def search_friend_by_username(user_id, nickname):
    query = "SELECT friend_id, nickname " \
            "FROM user_friend " \
            "WHERE user_id ='{}' and nickname like '%{}%'".format(user_id, nickname)

    list_friends = query_db(query, is_data_fetched=True)

    return list_friends

if __name__ == '__main__':
   print group_friend_by_lives_in(1)