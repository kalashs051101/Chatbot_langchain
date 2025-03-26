# import sqlite3

# class Database:
#     def __init__(self,db_name = "chatbot.db"):
#         self.conn = sqlite3.connect(db_name,check_same_thread=False)
#         self.cursor = self.conn.cursor()
#         self.create_tables()

#     def create_tables(self):
#         self.cursor.execute(
#             """ 
#             CREATE TABLE IF NOT EXISTS users(
#                 id integer primary key AUTOINCREMENT,
#                 user_id TEXT UNIQUE,
#                 native_language TEXT,
#                 learning_language TEXT,
#                 level TEXT
#             )

#             """
#         )
#         self.cursor.execute(
#             """ 
#             CREATE TABLE IF NOT EXISTS mistakes(
#                 id integer primary key AUTOINCREMENT,
#                 user_id TEXT,
#                 mistake TEXT,
#                 correction TEXT
#             )
#             """
#         )
#         self.conn.commit()

#     def add_user(self,user_id,native_language,learning_language,level):
#         self.cursor.execute(
#             """
#             INSERT OR IGNORE INTO users(
#             user_id,native_language,learning_language,level
#             )
#             VALUES(?,?,?,?)
#             """,
#             (user_id,native_language,learning_language,level)
#         )
#         print('i am herer =====')
#         self.conn.commit()
#         print('done iti is saved =====')

#     def log_mistake(self,user_id,mistake,correction):
#         self.cursor.execute("""
#             INSERT into mistakes (user_id,mistake,correction)values(?,?,?)""",
#             (user_id,mistake,correction)
#             )
#         self.conn.commit()

#     def get_mistake(self,user_id):
#         self.cursor.execute("""
#             select mistake,correction from mistakes where user_id = ?
#         """,(user_id,))

#         return self.cursor.fetchall()



import sqlite3

class Database:
    def __init__(self, db_name="chatbot.db"):
        """Initialize SQLite database."""
        self.conn = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        """Creates tables for users and mistakes."""
        self.cursor.execute(
            """ 
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                native_language TEXT,
                learning_language TEXT,
                level TEXT
            )
            """
        )
        self.cursor.execute(
            """ 
            CREATE TABLE IF NOT EXISTS mistakes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                mistake TEXT,
                correction TEXT
            )
            """
        )
        self.conn.commit()

    def add_user(self, user_id, native_language, learning_language, level):
        """Adds user to the database."""
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO users (user_id, native_language, learning_language, level)
            VALUES (?, ?, ?, ?)
            """,
            (user_id, native_language, learning_language, level)
        )
        self.conn.commit()

    def log_mistake(self, user_id, mistake, correction):
        """Logs a mistake in the database."""
        self.cursor.execute(
            """
            INSERT INTO mistakes (user_id, mistake, correction) VALUES (?, ?, ?)
            """,
            (user_id, mistake, correction)
        )
        self.conn.commit()

    def get_mistakes(self, user_id):
        """Retrieves all mistakes for a user."""
        self.cursor.execute(
            "SELECT mistake, correction FROM mistakes WHERE user_id = ?", (user_id,)
        )
        return self.cursor.fetchall()
