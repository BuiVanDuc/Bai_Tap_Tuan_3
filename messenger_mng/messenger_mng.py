AUTH_MENU = '''\nCHAT WITH YOUR FRIENDS!
1. Login
2. Register
3. Exit
'''

MAIN_MENU = '''\nMANAGE YOUR ACCOUNT
1. Messages
2. Friends
3. Logout
'''

MESSAGE_MENU = '''\nMANAGE YOUR MESSAGES
1. View
2. Send
3. Back to main
'''

FRIEND_MENU = '''\nMANAGE YOUR FRIENDS
1. View
2. Add
3. Remove
4. Block
5. Unblock
6. Back to Main
'''

'''
	0 --> auth menu
	1 --> main menu
	2 --> manage messages
	3 --> manage friends
'''


def display_menu(menu=0):
    if menu == 0:
        print(AUTH_MENU)
    elif menu == 1:
        print(MAIN_MENU)
    elif menu == 2:
        print(MESSAGE_MENU)
    elif menu == 3:
        print(FRIEND_MENU)
    else:
        print ("Invalid option, please choose: 0, 1 or 2")
        return -1

    try:
        option = raw_input("Choose your option: ")
        # print("You choosed: " + option)
        return int(option)
    except Exception as ex:
        print(ex)
        return -1
