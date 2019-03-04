from datetime import datetime

def validate_date(date_str, date_format="%d-%m-%Y"):
    try:
        date_obj = datetime.strptime(date_str, date_format)
        return date_obj
    except ValueError:
        print ("Format birth of date dd-mm-YYYY. Example: 11-12-1994")

def convert_datetime_to_string(date_time, type_format):
    if isinstance(date_time, datetime):
        if type_format == 1:
            date_time_str = date_time.strftime("%Y_%m_%d_T%H_%M_%S")
            return date_time_str
        elif type_format == 2:
            date_time_str = date_time.strftime("%Y_%m_%d")
            return date_time_str
    print "Input datetime not validate!"
    return 0
