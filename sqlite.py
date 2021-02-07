import _sqlite3


class Sql:
    def __init__(self, base_name):
        self.con = _sqlite3.connect(base_name)
        self.cur = self.con.cursor()

    def add_login(self, user_id, post):
        return self.cur.execute("""INSERT INTO login(user_id, post) VALUES(?,?)""", (user_id, post,))

    def del_log(self, user_id):
        return self.cur.execute("""DELETE FROM problem WHERE user_id=?""", (user_id,))

    def in_log(self, user_id):
        res = self.cur.execute("""SELECT * from login WHERE user_id=?""", (user_id,)).fetchall()
        return bool(len(res))

    def add_problem(self, type, address, description, solved):
        return self.cur.execute("""INSERT INTO problem(type, address, description, solved) VALUES(?,?,?,?)""", (type, address, description, solved,))

    def del_problem(self, id):
        return self.cur.execute("""DELETE FROM problem WHERE id=?""", (id,))
