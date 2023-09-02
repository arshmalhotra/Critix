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
# Sample Code:

# with connection:
#     with connection.cursor() as cursor:
#         # Create a new record
#         sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
#         cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
#
#     # connection is not autocommit by default. So you must commit to save
#     # your changes.
#     connection.commit()
#
#     with connection.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
#         cursor.execute(sql, ('webmaster@python.org',))
#         result = cursor.fetchone()
#         print(result)

def getUserSpecificSalt(user: User, response: GetSignInChallengeResponse):
    with connection:
        with connection.cursor() as cursor:
            sql = '''
                SELECT `password_salt`
                FROM `Users`
                WHERE `email`=%s OR `username`=%s
            '''
            cursor.execute(sql, (user.getEmail(), user.getUsername(),))
            # fetches first result
            # modify if need to parse
            result = cursor.fetchone()

            response.setPasswordSalt(result)
