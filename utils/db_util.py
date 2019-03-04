import sqlite3

from message_mng.settings import DATABASE_PATH


def connect_to_sqlite(db_path=DATABASE_PATH):
    try:
        # connect to the sqlite server
        conn = sqlite3.connect(db_path)
        if conn is not None:
            print('Successfully connect to Database')
            return conn
    except (Exception, sqlite3.DatabaseError) as error:
        print ("CONNECTING TO THE DB IS ERROR" + ":" + str(error))


def query_db(query, is_data_fetched=False):
    try:
        conn = connect_to_sqlite()
        if conn is not None:
            # create a cursor
            cur = conn.cursor()
            # execute a statement
            if is_data_fetched:
                list_data = dict_gen(cur.execute(query))
                conn.commit()
                # close communication with the database
                cur.close()
                return list_data

            cur.execute(query)

            if cur.rowcount ==1 or cur.lastrowid:
                conn.commit()
                # close communication with the database
                cur.close()
                return 1

            return 0

    except (Exception, sqlite3.DatabaseError) as error:
        print('Query is not valid' + ":" + str(error))
    return 0


def dict_gen(curs):
    ''' From Python Essential Reference by David Beazley
    '''
    import itertools
    field_names = [d[0].lower() for d in curs.description]

    rows = curs.fetchall()
    if not rows:
        return
    list_data = list()
    for row in rows:
        list_data.append(dict(itertools.izip(field_names, row)))

    return list_data
