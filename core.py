import sqlite3
from pathlib import Path

# создание и подключение базы данных
class DataBase:
    def __init__(self):
        self.Path_db = Path("DB.sqlite3")
        self.con = sqlite3.connect(str(self.Path_db))
        self.con.row_factory = sqlite3.Row

    def __del__(self):
        self.con.close()

    # методы для отправки запросов
    def exec_write(self, sql: str, parms: tuple | list[tuple] = None):
        cur = self.con.cursor()

        if sql == None:
            cur.execute(sql)

        elif isinstance(parms, list):
            cur.executemany(sql, parms)

        else:
            cur.execute(sql, parms)
        self.con.commit()

    def exec_script(self, sql:str):
        cur = self.con.cursor()
        cur.executescript(sql)
        self.con.commit()

    # метод для чтения данных с БД
    def exec_read(self, sql: str, parms: tuple | list[tuple] = ()):
        cur = self.con.cursor()
        
        row = cur.execute(sql, parms)
        lst_dict = []
        for val in row:
            lst_dict.append(dict(val))
        
        return lst_dict