import  sqlite3
class Database():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students(studentID INTEGER  PRIMARY KEY AUTOINCREMENT, name text, surname text, program text, gender text, phone text)")
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS userlog(username TEXT  PRIMARY KEY , password text)")
        self.conn.commit()
    def getUser(self):
        self.cur.execute("SELECT username=?, password=? FROM userlog")
        rows = self.cur.fetchone()
        return rows

    def fetch(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        return rows

    def insert(self, studentID, name, surname, program, gender, phone):
        self.cur.execute("INSERT INTO students VALUES(NULL, ?, ?,? ,?,?)", (studentID,name, surname, program, gender, phone))
        self.conn.commit()
    def update(self, studentID, name, surname, program, gender, phone):
        self.cur.execute("UPDATE students SET name=?, surname=?, program=?, gender=?, phone=? WHERE studentID=?", (name, surname, program, gender, phone, studentID))
        self.conn.commit()
    def delete(self, studentID):
        self.cur.execute("DELETE FROM students WHERE studentID=? ", (studentID,))
        self.conn.commit()
    def __del__(self):
        self.conn.close()


db = Database("studentDB.db")
