import unittest
import sqlite3

class TestLogin(unittest.TestCase):
    def test_user_exists(self):
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username='admin' AND password='admin123'")
        result = cursor.fetchone()
        conn.close()
        self.assertIsNotNone(result)

if __name__ == "__main__":
    unittest.main()
