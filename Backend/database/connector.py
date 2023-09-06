import pymysql.cursors
from pymysql import InternalError, DatabaseError
from Components.User import User

host = ''
user = ''
password = ''
database = ''

# Connect to the database
# connection = pymysql.connect(host=host,
#                              user=user,
#                              password=password,
#                              database=database,
#                              cursorclass=pymysql.cursors.DictCursor)

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

def getUserId(user: User) -> None:
    with connection:
        with connection.cursor() as cursor:
            sql = '''
                SELECT `user_id`
                FROM `Users`
                WHERE `email`=%s OR `username`=%s
            '''
            rows = cursor.execute(sql, (user.getEmail(), user.getUsername(),))
            if rows == 0:
                raise ValueError(
                    f'No user found: ({user.getEmail()}, {user.getUsername()})'
                )
            if rows != 1:
                raise InternalError(
                    f'Too many users matching: ({user.getEmail()},'
                    f' {user.getUsername()})'
                )

            userId = cursor.fetchone()
            user.setUserId(userId)

def getUserPasswordHash(user: User) -> None:
    with connection:
        with connection.cursor() as cursor:
            sql = '''
                SELECT `password_hash`
                FROM `Users`
                WHERE `email`=%s OR `username`=%s
            '''
            rows = cursor.execute(sql, (user.getEmail(), user.getUsername(),))
            if rows == 0:
                raise ValueError(
                    f'No user found: ({user.getEmail()}, {user.getUsername()})'
                )
            if rows != 1:
                raise InternalError(
                    f'Too many users matching: ({user.getEmail()},'
                    f' {user.getUsername()})'
                )
            # fetches first result
            # modify if need to parse
            passwordHash = cursor.fetchone()
            user.setPasswordHash(passwordHash)

def getUserSpecificSalt(user: User) -> None:
    with connection:
        with connection.cursor() as cursor:
            sql = '''
                SELECT `password_salt`
                FROM `Users`
                WHERE `email`=%s OR `username`=%s
            '''
            rows = cursor.execute(sql, (user.getEmail(), user.getUsername(),))
            if rows == 0:
                raise ValueError(
                    f'No user found: ({user.getEmail()}, {user.getUsername()})'
                )
            if rows != 1:
                raise InternalError(
                    f'Too many users matching: ({user.getEmail()},'
                    f' {user.getUsername()})'
                )
            # fetches first result
            # modify if need to parse
            passwordSalt = cursor.fetchone()
            user.setPasswordSalt(passwordSalt)

def storeTemporaryNonce(user: User) -> None:
    with connection:
        with connection.cursor() as cursor:
            sql = f'''
                UPDATE `Users`
                SET `temporary_nonce` = {user.getTemporaryNonce()}
                WHERE `email`=%s OR `username`=%s
            '''
            rows = cursor.execute(sql, (user.getEmail(), user.getUsername(),))

        if rows != 1:
            connection.rollback()
            raise DatabaseError(
                f'Error updating user ({user.getEmail()}, {user.getUsername()})'
                f' with server nonce'
            )
        connection.commit()

def getTemporaryNonce(user: User) -> None:
    with connection:
        with connection.cursor() as cursor:
            sql = '''
                SELECT `temporary_nonce`
                FROM `Users`
                WHERE `email`=%s OR `username`=%s
            '''
            cursor.execute(sql, (user.getEmail(), user.getUsername(),))
            # TODO verify if there's only 1?
            # fetches first result
            # modify if need to parse
            serverNonce = cursor.fetchone()

            # Delete server nonce from database
            user.setTemporaryNonce(None)
            storeTemporaryNonce(user)

            # Set server nonce for user
            user.setTemporaryNonce(serverNonce)
