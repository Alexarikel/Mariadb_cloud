import mariadb
import logging


class Db_operations:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.conn = self.connection()

    def connection (self):
        conn = mariadb.connect(
            user = self.user,
            password = self.password,
            host = self.host,
            port = self.port,
            database = self.database
        )
        return conn

    def insert (self, table, file_name):
        with open (file_name, mode="r") as downloaded:
            for line in downloaded.readlines():
                try:
                    line = line.strip().split(",")
                    sqlquery = f"INSERT INTO {table} VALUES {*line,}"
                    curr = self.conn.cursor()
                    curr.execute(sqlquery)
                except mariadb.Error as e:
                    logging.error(e)
                    return False
            self.conn.commit()