import pymysql

def get_connection():
    try:
        conn = pymysql.connect(
            host="localhost",
            database="malaguenos",
            user="root",
            passwd=""
        )
        return conn
    except Exception as ex:
        print(ex)
        return None
