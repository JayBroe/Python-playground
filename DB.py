import sqlite3

class DB:
    con = sqlite3.connect("database.db")
    cursor = con.cursor()
    
    def clear_base(self):
        sql = "DELETE FROM colors"
        sql1 = "DELETE FROM bar_info"
        sql_2 = "UPDATE variables SET index_1 = (?), index_2 = (?)"
        DB.cursor.execute(sql)
        DB.cursor.execute(sql1)
        DB.cursor.execute(sql_2, [0,0])
        DB.con.commit()
        DB.con.close    

    def add_3elements(self, table, data, ID):
        sql = f"INSERT INTO {table} (v1, v2, v3, ID) VALUES(?,?,?,?)"
        DB.cursor.execute(sql, 
                    [data[0], data[1], data[2], ID])
        DB.con.commit()
        DB.con.close

    def if_empty(self, table):
        sql = f"SELECT COUNT(*) FROM {table}"
        DB.cursor.execute(sql)
        DB.con.commit()
        DB.con.close
        res = DB.cursor.fetchone()
        self.ID = res
        if self.ID is None:
            return 0    

    def fetch_one(self, table, data):
        sql = f"SELECT {data} FROM {table}"
        DB.cursor.execute(sql)
        DB.con.commit()
        DB.con.close  
        res = DB.cursor.fetchone()
        return res[0]
    
    def update_value(self, table, data, val):
        sql = f"UPDATE {table} SET {data} = (?)"
        DB.cursor.execute(sql, 
                    [val])
        DB.con.commit()
        DB.con.close 

    def insert_2elements(self, table, element1, element2):
        sql = f"INSERT INTO {table} VALUES(?,?)"
        DB.cursor.execute(sql, 
                    [element1,element2])
        DB.con.commit()
        DB.con.close

    def fetch_color(self,ID):
        sql = "SELECT v1,v2,v3 FROM colors WHERE ID = (?)"
        DB.cursor.execute(sql, [ID])
        DB.con.commit()
        DB.con.close  
        res = DB.cursor.fetchall()
        self.ID = res
        for r in self.ID:
            return r    