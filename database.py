import sqlite3
from sqlite3 import Error
import os


class Database:
    conn = None

    def __init__(self):
        self.__create_connection()

    def __create_connection(self):
        """ create a database connection to a SQLite database """
        try:
            if not self.conn:
                DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
                self.conn = sqlite3.connect(DEFAULT_PATH)

        except Error as e:
            print(e)
        finally:
            if self.conn:
                self.__setup_tables()
                return self.conn

    def __setup_tables(self):
        try:
            if self.conn:
                cur = self.conn.cursor()
                cur.execute("CREATE TABLE IF NOT EXISTS account(accountId INTEGER constraint account_pk primary key autoincrement, email varchar(255), password varchar(255), disabled INTEGER default 0 not null);")
                cur.execute("CREATE UNIQUE INDEX account_email_uindex on account (email);")
                cur.execute("CREATE TABLE IF NOT EXISTS account_connection (accountConnectionId INTEGER constraint account_connection_pk primary key autoincrement, protocol varchar(10) not null, connection_url varchar(255) not null, accountId INTEGER, constraint account_connection_account__accountId_fk foreign key (accountId, accountId) references account ("", accountId) on update cascade on delete cascade);")
                cur.close()
        except Error as e:
            print(e)

    def run(self, sql):
        try:
            if self.conn:
                cur = self.conn.cursor()
                cur.execute(sql)
                cur.close()
                return True
        except Error as e:
            print(e)
            return False

    def select(self, sql):
        if self.conn:
            cur = self.conn.cursor()
            cur.execute(sql)

            rows = cur.fetchall()
            cur.close()
            return rows

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print('Database connection closed')
