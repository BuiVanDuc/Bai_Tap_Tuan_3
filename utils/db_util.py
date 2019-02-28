import psycopg2

from utils.file_util import load_config
from psycopg2.extras import RealDictCursor

def connect_to_pgsql(config_filename):
    try:
        # read connection parameters
        params = load_config(config_filename)
        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        if conn is not None:
            print('Successfully connect to pgsql')
            return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print ("CONNECTING TO THE PGSQL IS ERROR" + ":" + str(error))


def query_db(query, config_filename='database.json', is_fetching_data=False):
    try:
        conn = connect_to_pgsql(config_filename)
        if conn is not None:
            # create a cursor
            cur = conn.cursor(cursor_factory=RealDictCursor)
            # execute a statement
            cur.execute(query)
            status= cur.statusmessage

            if is_fetching_data:
                data = cur.fetchall()
                # commit the changes to the database
                conn.commit()
                # close communication with the database
                cur.close()
                return data
            # commit the changes to the database
            conn.commit()
            # close communication with the database
            cur.close()
            if int(status[-1]) > 0:
                return 1
            return 0
    except (Exception, psycopg2.DatabaseError) as error:
        print('Query is not valid' + ":" + str(error))
    return 0
