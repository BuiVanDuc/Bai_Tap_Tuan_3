from functions import group_friend_by_lives_in, detail_friend, is_friend_existed, \
    add_friend, search_friend, view_friends, remove_friend, view_friends_by_contact_time
from messages.functions import sent_message
from messenger_mng.messenger_mng import display_menu
from users.functions import block, remove_block, view_list_block, is_blocked
from users.functions import search_username


def display_search_friend(user_id, username):
    list_friends = search_friend(user_id, username)

    if list_friends and len(list_friends) > 0:
        print list_friends
        try:
            print "Choose number in list to sent message"
            index = raw_input('Choose number:\t')
            index = int(index)
            friend_id = index - 1
            if friend_id in list_friends['user_id']:
                return friend_id
            else:
                print "Invalid option, please choose number in list"
                return -1
        except Exception as Ex:
            print (Ex)
            return -1
    else:
        print 'No results found'
        return -1


def display_group_friend_by_city(user_id):
    list_friends = group_friend_by_lives_in(user_id)

    if list_friends and len(list_friends) > 0:
        try:
            print '''
                   0: Exit
                   Other number(in list): view detail a friend
            '''
            index = raw_input('Choose number:\t')
            index = int(index)
            if index == 0:
                print "Exit"
            elif index > 0:
                friend_id = index - 1
                if friend_id in list_friends['user_id']:
                    return friend_id
            else:
                print "Invalid option, please choose number in list"
                return -1
        except Exception as Ex:
            print (Ex)
            return -1
    else:
        print "No Friends"


def display_list_friend(user_id):
    list_friends = view_friends(user_id)

    if list_friends and len(list_friends) > 0:
        print list_friends
        try:
            print "Choose number in list to sent message"
            index = raw_input('Choose number:\t')
            index = int(index)
            friend_id = index - 1
            if friend_id in list_friends['user_id']:
                print "To {}".format(list_friends[friend_id]['name'])
                return friend_id
            else:
                print "Invalid option, please choose number in list"
                return -1
        except Exception as Ex:
            print (Ex)
            return -1
    else:
        print "Have no friend"
        return -1


def display_view_friends_by_contact_time(user_id):
    list_friends = view_friends_by_contact_time(user_id)

    if list_friends and len(list_friends) > 0:
        index = 0
        for friend in list_friends:
            index += 1
            print "{}. {}".format(index, friend['nickname'])

        try:
            print '''
                    0: Exit
                    Other number (in list): view detail a friend
                  '''

            number = int(raw_input("Choose number:\t"))

            if number == 0:
                print "Exit"
            elif 0 < number <= len(list_friends):
                index = number - 1
                friend_id = list_friends[index]['friend_id']
                friend = detail_friend(friend_id)

                for key, val in friend[0].items():
                    print key, ":", val

                print'''
                        0: Exit
                        1: Reply
                    '''

                number = int(raw_input("Choose number:\t"))
                if number == 0:
                    print "Exit"
                elif number == 1:
                    print "To {}".format(list_friends[index]['nickname'])
                    message_content = raw_input("Type a message:\t")
                    if message_content and len(message_content) > 0:
                        if is_blocked(user_id, friend_id) ==1:
                            print "You have blocked {}. Unblock to sent message!!".format(list_friends[index]['nickname'])
                            return -1
                        if is_blocked(friend_id, user_id) ==2:
                            print "You were blocked by {}. Can not sent message!!.".format(list_friends[index]['nickname'])
                            return -1
                        elif is_blocked(friend_id, user_id) == 0:
                            if sent_message(friend_id, message_content, user_id):
                                print "Sent message successfully!!"
                        else:
                            print "Can not sent message"
                    else:
                        print "Message content is empty"
                        return -1
                else:
                    print "Invalid option, please choose: 0 or 1"
                    return -1
            else:
                print "Invalid option"
                return -1

        except Exception as Ex:
            print (Ex)
            return -1
    else:
        print 'No Friend'


def display_view_friend(user_id):
    while True:
        print '''
            1. List friends
            2. Group friends by city
            3. Exit
            '''
        try:
            option = int(raw_input('Choose option:\t'))
            if option == 1:
                display_view_friends_by_contact_time(user_id)
            elif option == 2:
                groups_city = group_friend_by_lives_in(user_id)

                if groups_city and len(groups_city) > 0:
                    for key, val in groups_city.items():
                        print key
                        index = 0
                        count = 0
                        for username in val:
                            index += 1
                            print "{}. {}".format(index, username)
                        count += 1
                else:
                    print "No Friend"
            elif option == 3:
                break
            else:
                print "Invalidate option, please option 1, 2 or 3"
        except Exception as Ex:
            print (Ex)
            return -1


def display_add_friend(user_id):
    try:
        username = raw_input("Search:\t")
        if username and len(username) > 0:
            list_username = search_username(username)

            if list_username and len(list_username) > 0:
                index = 0

                for username in list_username:
                    index += 1
                    print "{}. {}".format(index, username['username'])

                print "Choose number (in list) to add friend"
                number = int(raw_input("number:\t"))

                if 0 < number <= len(list_username):
                    index = number - 1
                    friend_id = list_username[index]['id']
                    username = list_username[index]['username']
                    # Check friend is existed:
                    if is_friend_existed(user_id, friend_id):
                        print "Can not add.Friend is existed !!"
                        return -1
                    else:
                        if friend_id == user_id:
                            print "Can not add friends with yourself!!"
                            return -1
                        elif add_friend(user_id, friend_id, username):
                            print "Add friend successfully"
                        else:
                            print "Can not add friend!!"
                            return -1
                else:
                    print "Invalid number, please try again!!"
                    return -1
            else:
                print "No result"
                return -1
        else:
            print "username is empty. please enter a username"
            return -1
    except Exception as Ex:
        print (Ex)
        return -1


def display_remove_friend(user_id):
    try:
        list_friend = view_friends_by_contact_time(user_id)

        if list_friend and len(list_friend) > 0:
            index = 0
            for friend in list_friend:
                index += 1
                print "{}. {}".format(index, friend['nickname'])

            print "Choose number in list friend to remove"
            number = int(raw_input("Number:\t"))
            if 0 < number <= len(list_friend):
                index = number - 1
                friend_id = list_friend[index]['friend_id']
                if remove_friend(user_id, friend_id):
                    print "Remove successfully!!"
                else:
                    print "Can not Remove"
            else:
                print "Invalid option, please try again"
        else:
            print "No friend"
    except Exception as Ex:
        print(Ex)
        return -1


def display_block_friend(user_id):
    try:
        list_friend = view_friends_by_contact_time(user_id)

        if list_friend and len(list_friend) > 0:
            index = 0
            for friend in list_friend:
                index += 1
                print "{}. {}".format(index, friend['nickname'])

            print "Choose number in list friend block"
            number = int(raw_input("Number:\t"))
            if 0 < number <= len(list_friend):
                index = number - 1
                friend_id = list_friend[index]['friend_id']
                if is_blocked(user_id, friend_id) == 1:
                    print "Bock is existed!!"
                    return -1
                else:
                    if block(user_id, friend_id):
                        print "Block successfully!!"
            else:
                print "Invalid option, please try again"
                return -1
        else:
            print "No friends"
            return -1
    except Exception as Ex:
        print(Ex)
        return -1


def display_unblock(user_id):
    try:
        list_block = view_list_block(user_id)
        if list_block and len(list_block) > 0:
            index = 0
            for user in list_block:
                index += 1
                print "{} .{}".format(index, user['username'])

            print "Choose number (in list): to delete"
            number = int(raw_input("Number:\t"))
            if 0 < number <= len(list_block):
                index = number - 1
                user_id_blocked = list_block[index]['user_id_blocked']
                if remove_block(user_id, user_id_blocked):
                    print "Unblock successfully!!"
            else:
                print "Invalid option, please try again"
        else:
            print "No friend is blocked"
    except Exception as Ex:
        print (Ex)
        return -1


def friends(user_id):
    while True:
        option = display_menu(3)
        if option == 1:
            '''
                View
            '''
            display_view_friend(user_id)
        elif option == 2:
            '''
                Add friend
            '''
            display_add_friend(user_id)
        elif option == 3:
            '''
                Remove
            '''
            display_remove_friend(user_id)
        elif option == 4:
            '''
                Block
            '''
            display_block_friend(user_id)
        elif option == 5:
            '''
                unblock
            '''
            display_unblock(user_id)
        elif option == 6:
            print "Back to main"
            break