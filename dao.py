import sqlite3

class VotingDAO:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS votes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            candidate_id INTEGER,
            FOREIGN KEY(user_id) REFERENCES users(id),
            FOREIGN KEY(candidate_id) REFERENCES candidates(id)
        )''')

        self.conn.commit()

    def add_user(self, username, password):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False

    def check_user(self, username, password):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
        result = cursor.fetchone()
        return result[0] if result else None

    def get_candidates(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, description FROM candidates")
        return cursor.fetchall()

    def vote(self, user_id, candidate_id):
        cursor = self.conn.cursor()
        # Проверим, голосовал ли уже этот пользователь
        cursor.execute("SELECT * FROM votes WHERE user_id = ?", (user_id,))
        if cursor.fetchone():
            return False  # Уже голосовал
        cursor.execute("INSERT INTO votes (user_id, candidate_id) VALUES (?, ?)", (user_id, candidate_id))
        self.conn.commit()
        return True

