from database.connection_pool import ConnectionPool

from mysql.connector.errors import InternalError, DatabaseError
from components.user import User
from typing import Tuple, Any
import json

'''
Create db_config.json structured
{
    'user':
    'password':
    'host':
    'port':
    'database':
}
'''
with open('database/db_config.json') as config_file:
    config = json.load(config_file)
connection_pool = ConnectionPool(**config)


##############
# Query verification methods
##############
def _verify_no_user_found(conn: Any, cursor: Any, args: Tuple[Any]) -> None:
    rows = cursor.rowcount
    if rows == 1:
        raise ValueError(f'User was found for: {args}')
    if rows > 1:
        raise DatabaseError(f'Too many users found for: {args}')

def _verify_single_user_found(conn: Any, cursor: Any, args: Tuple[Any]) -> None:
    rows = cursor.rowcount
    if rows == 0:
        raise ValueError(f'No user found: {args}')
    if rows != 1:
        raise InternalError(f'Too many users matching: {args}')

def _verify_single_update(conn, cursor, args):
    rows = cursor.rowcount
    if rows != 1:
        conn.rollback()
        raise DatabaseError(f'Error updating user {args}')


##############
# Query methods
##############

def validateNewUser(user: User) -> None:
    sql = '''
        SELECT `user_id`
        FROM `Users`
        WHERE `email`=%s OR `username`=%s OR `phone_number`=%s
    '''
    params = (user.getEmail(), user.getUsername(), user.getPhoneNumber())
    result = connection_pool.execute(sql,
                                     args=params,
                                     verify_rows=_verify_no_user_found)

def createNewUser(user: User) -> None:
    sql = '''
        INSERT INTO `Users`
        (`username`, `email`, `password_hash`, `password_salt`, `phone_number`, `name`, `profile_picture`)
        VALUES (%(username)s, %(email)s, %(passwordHash)s, %(passwordSalt)s, %(phoneNumber)s, %(name)s, %(profilePicture)s)
    '''
    params = {attr.split('__', 1)[1]: val for attr, val in user.__dict__.items()}
    result = connection_pool.execute(sql,
                                     args=params,
                                     commit=True,
                                     verify_rows=_verify_single_update)
    # result provides user_id on successful insert
    user.setUserId(result)

def getFullUser(user: User) -> None:
    sql = '''
        SELECT *
        FROM `Users`
        WHERE `email`=%s OR `username`=%s
    '''
    params = (user.getEmail(), user.getUsername())
    result = connection_pool.execute(sql,
                                     args=params,
                                     verify_rows=_verify_single_user_found)

    row = result[0]
    user.setUserId(
            row[0]
        ).setUsername(
            row[1]
        ).setEmail(
            row[2]
        ).setPasswordHash(
            _rencode_byte_result(row[3]),
            _rencode_byte_result(row[4])
        ).setPhoneNumber(
            row[5]
        ).setName(
            row[6]
        )

def getUserPasswordHash(user: User) -> None:
    sql = '''
        SELECT `password_hash`
        FROM `Users`
        WHERE `email`=%s OR `username`=%s
    '''
    params = (user.getEmail(), user.getUsername())
    result = connection_pool.execute(sql,
                                     args=params,
                                     verify_rows=_verify_single_user_found)
    # fetches first result
    # modify if need to parse
    passwordHash = _rencode_byte_result(result[0][0])
    user.setPasswordHash(passwordHash=passwordHash)

def getUserSpecificSalt(user: User) -> None:
    sql = '''
        SELECT `password_salt`
        FROM `Users`
        WHERE `email`=%s OR `username`=%s
    '''
    params = (user.getEmail(), user.getUsername())
    result = connection_pool.execute(sql,
                                     args=params,
                                     verify_rows=_verify_single_user_found)

    passwordSalt = _rencode_byte_result(result[0][0])
    user.setPasswordHash(passwordSalt=passwordSalt)

def storeTemporaryNonce(user: User) -> None:
    sql = '''
        UPDATE `Users`
        SET `temporary_nonce` = %s
        WHERE `email`=%s OR `username`=%s
    '''
    params = (user.getTemporaryNonce(),user.getEmail(), user.getUsername())
    result = connection_pool.execute(sql,
                                     args=params,
                                     commit=True,
                                     verify_rows=_verify_single_update)

def getTemporaryNonce(user: User) -> None:
    sql = '''
        SELECT `temporary_nonce`
        FROM `Users`
        WHERE `email`=%s OR `username`=%s
    '''
    params = (user.getEmail(), user.getUsername())
    result = connection_pool.execute(sql,
                                     args=params,
                                     verify_rows=_verify_single_user_found)
    # fetches first result
    # modify if need to parse
    serverNonce = _rencode_byte_result(result[0][0])

    # Delete server nonce from database
    user.setTemporaryNonce(None)
    storeTemporaryNonce(user)

    # Set server nonce for user
    user.setTemporaryNonce(serverNonce)

##############
# Helper methods
##############
def _rencode_byte_result(result: Any) -> Any:
    return result.decode().encode('raw_unicode_escape')
