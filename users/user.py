from functions import login, get_id, is_email_existed
from functions import register
from utils.date_util import validate_date
from utils.email_util import is_email_validated
from utils.password_util import encrypt_string, validate_password


def display_login():
    username = raw_input("username:\t")
    if username and len(username) > 0:
        password = raw_input("password:\t")
        if password and len(password) > 0:
            password = encrypt_string(password)

            if login(username, password):
                user_id = get_id(username, password)
                return user_id
            else:
                print "username, password is incorrect"
                return -1
        else:
            print "password is empty!!"
            return -1
    else:
        print "username is emtpy!!"
        return -1


def display_register():
    email, fullname, birth_of_date, username, password, lives_in = "", "", "", "", "", ""
    sex = 1
    flag = 0
    while True:
        if is_email_validated(email):
            if is_email_existed(email):
                print "email account have existed. Please enter other email !!"
                email = ""
            else:
                if len(fullname) > 0:
                    if flag:
                        pass
                    else:
                        try:
                            print "(Sex) 0 -> male,1 -> female, Other"
                            sex = int(raw_input('Sex:\t'))
                            print "lives in can be empty"
                            lives_in = raw_input("lives_in:\t")
                            flag = 1
                        except Exception as Ex:
                            print (Ex)
                            return -1
                    if validate_date(birth_of_date):
                        if len(username) > 0:
                            if validate_password(password):
                                confirm_password = raw_input("confirm_password:\t")
                                if confirm_password == password:
                                    password = encrypt_string(password)
                                    if register(email, fullname, birth_of_date, sex, username,
                                                password,
                                                lives_in):
                                        print "Register successfully"
                                        break
                                    else:
                                        print "Can not register"
                                        break
                                else:
                                    print "Password confirmation doesn't match password"
                            else:
                                password = raw_input("Password:\t")
                        else:
                            username = raw_input("Username:\t")
                            if len(username) < 0:
                                print " username is empty. Please enter your username"
                    else:
                        birth_of_date = raw_input("Date of birth:\t")
                else:
                    fullname = raw_input("Fullname:\t")
                    if len(fullname) < 0:
                        print " fullname is empty. Please enter your fullname"
        else:
            email = raw_input("email:\t")
            if not is_email_validated(email):
                print "email is invalidated. Please enter email again!!"