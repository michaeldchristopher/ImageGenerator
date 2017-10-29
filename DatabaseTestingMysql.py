import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='192.168.1.247',
                             user='michael',
                             password='lindamarie',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('anyone', 'not-very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('anyone',))
        result = cursor.fetchone()
        print(result)
        sql = "SELECT `id`, `password` FROM `users`"
        cursor.execute(sql, ())
        result = cursor.fetchall ()
        print(result)
finally:
    connection.close()