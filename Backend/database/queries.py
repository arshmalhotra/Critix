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

def getUserId(user: User) -> None:
    sql = '''
        SELECT `user_id`
        FROM `Users`
        WHERE `email`=%s OR `username`=%s
    '''
    params = (user.getEmail(), user.getUsername())
    result = connection_pool.execute(sql,
                                     args=params,
                                     verify_rows=_verify_single_user_found)

    userId = _get_first_from_result(result)
    user.setUserId(userId)

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
    passwordHash = _get_first_from_result(result).decode(
                                                ).encode('raw_unicode_escape')
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

    passwordSalt = _get_first_from_result(result).decode(
                                                ).encode('raw_unicode_escape')
    print(passwordSalt)
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
    serverNonce = _get_first_from_result(result).decode(
                                               ).encode('raw_unicode_escape')

    # Delete server nonce from database
    user.setTemporaryNonce(None)
    storeTemporaryNonce(user)

    # Set server nonce for user
    user.setTemporaryNonce(serverNonce)

##############
# Helper methods
##############
def _get_first_from_result(result: Any) -> Any:
    return result[0][0]
