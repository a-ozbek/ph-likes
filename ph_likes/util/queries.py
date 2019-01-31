import psycopg2
from ph_likes.util import settings


def get_connection_cursor():
    conn_string = "host='{HOST_NAME}' dbname='{DB_NAME}' user='{USER}' password='{PASSWORD}'".\
    format(HOST_NAME=settings.PRH_HOST, 
           DB_NAME=settings.PRH_DBNAME, 
           USER=settings.PRH_USER, 
           PASSWORD=settings.PRH_PASSWORD)
    conn = psycopg2.connect(conn_string)
    cur = conn.cursor()
    return cur


def get_table_names():
    query = "select relname from pg_class where relkind='r' and relname !~ '^(pg_|sql_)';"
    cur = get_connection_cursor()
    cur.execute(query)
    table_names = cur.fetchall()
    return table_names


def get_post_table():
    pass


def get_postlike_table():
    pass


def get_phuser_table():
    pass