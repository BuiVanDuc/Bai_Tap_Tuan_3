from friends.friend import friends
from messages.message import messages
from messenger_mng.messenger_mng import display_menu
from users.functions import logout
from users.user import display_login, display_register
from utils.db_utils.db_collection import connect_to_sqlite


def main(user_id):
    while True:
        option = display_menu(1)
        if option == 1:
            messages(user_id)
        elif option == 2:
            friends(user_id)
        elif option == 3:
            logout(user_id)
            break
        else:
            print ("Invalid option, please choose: 1, 2 or 3")


def auth():
    while True:
        option = display_menu(0)
        if option == 1:
            user_id = display_login()
            if user_id != -1:
                main(user_id)
        elif option == 2:
            display_register()
        elif option == 3:
            return -1


if __name__ == '__main__':
    # Check conect to db
    if connect_to_sqlite():
        auth()
    else:
        print "Can not connect DB"
