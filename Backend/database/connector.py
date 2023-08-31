import pymysql.cursors

host = ''
user = ''
password = ''
database = ''

# Connect to the database
connection = pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)

with connection:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)

def getUserSpecificSalt(user: User, authChallenge: AuthenticationChallenge):
    with connection:
        with connection.cursor() as cursor:
            sql = "SELECT `salt` FROM `Users` WHERE `email`=%s"
            cursor.execute(sql, (user.getEmail(),))
            result = cursor.fetchone()
            if result != None: # TODO: check return possibilities
                authChallenge.setSalt(result)
