import mysql.connector # type: ignore

db_config = {
    'user': 'root',
    'password': '',
    'host': '127.0.0.1',
    'database': 'perpustakaan'
}

def get_connection():
    return mysql.connector.connect(**db_config)
