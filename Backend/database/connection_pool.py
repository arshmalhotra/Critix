import time
import mysql.connector.pooling
from typing import Tuple, Any

class ConnectionPool(object):
    '''
    create a pool when connect mysql, which will decrease the time spent in
    request connection, create connection and close connection.
    '''
    def __init__(self, host: str = '172.0.0.1', port: str = '3306',
        user: str = 'root', password: str = '', database: str = 'test',
        pool_name: str = 'critix_pool', pool_size: int = 3
    ):
        res = {}
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._database = database

        res['host'] = self._host
        res['port'] = self._port
        res['user'] = self._user
        res['password'] = self._password
        res['database'] = self._database
        self.dbconfig = res
        self.pool = self._create_pool(pool_name=pool_name, pool_size=pool_size)

    def _create_pool(self, pool_name: str, pool_size: int):
        '''
        Create a connection pool, after created, the request of connecting
        MySQL could get a connection from this pool instead of request to
        create a connection.
        :param pool_name: the name of pool, default is 'mypool'
        :param pool_size: the size of pool, default is 3
        :return: connection pool
        '''
        pool = mysql.connector.pooling.MySQLConnectionPool(
            pool_name=pool_name,
            pool_size=pool_size,
            pool_reset_session=True,
            **self.dbconfig)
        return pool

    def close(self, conn: Any, cursor: Any):
        '''
        A method used to close connection of mysql.
        :param conn:
        :param cursor:
        :return:
        '''
        cursor.close()
        conn.close()

    def get_connection_and_cursor(self):
        '''
        A method to get a connection and its cursor from the pool.
        :return: connection and cursor
        '''
        conn = self.pool.get_connection()
        return conn, conn.cursor()

    def execute(self, sql: str, args: Tuple[Any] = None, commit: bool = False, verify_rows: Any = None):
        '''
        Execute a sql, it could be with args and with out args. The usage is
        similar with execute() function in module pymysql.
        :param sql: sql clause
        :param args: args need by sql clause
        :param commit: whether to commit
        :return: row count, if commit, return statement, else, return result
        '''
        # get connection from connection pool instead of create one.
        conn = self.pool.get_connection()
        cursor = conn.cursor()
        cursor.execute(sql, params=args)

        result = None
        if commit is True:
            conn.commit()
            result = cursor.statement
        else:
            result = cursor.fetchall()

        if verify_rows:
            verify_rows(conn, cursor, args)

        self.close(conn, cursor)
        return result
