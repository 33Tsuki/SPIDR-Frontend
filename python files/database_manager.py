import sqlite3
import os
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="thermo_med_cases.db"):
        self.db_path = db_path
        self.initialize_db()

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def initialize_db(self):
        """Initialize the database with the cases table if it doesn't exist."""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cases (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_number TEXT UNIQUE NOT NULL,
                    target_organ TEXT,
                    timestamp TEXT,
                    seg_path TEXT,
                    img_path TEXT,
                    status TEXT,
                    notes TEXT
                )
            ''')
            
            conn.commit()
            print(f"Database initialized at {self.db_path}")
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
        finally:
            if conn:
                conn.close()

    def add_case(self, case_number, target_organ, status="Initialized"):
        """Add a new case to the database."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT INTO cases (case_number, target_organ, timestamp, status)
                VALUES (?, ?, ?, ?)
            ''', (case_number, target_organ, timestamp, status))
            
            conn.commit()
            print(f"Case {case_number} added successfully.")
            return True
        except sqlite3.IntegrityError:
            print(f"Case {case_number} already exists.")
            return False
        except sqlite3.Error as e:
            print(f"Error adding case: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def update_case_files(self, case_number, seq_path, img_path):
        """Update the file paths for a specific case."""
        conn = None
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE cases 
                SET seg_path = ?, img_path = ?, status = 'Files Selected'
                WHERE case_number = ?
            ''', (seq_path, img_path, case_number))
            
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error updating case files: {e}")
            return False
        finally:
            if conn:
                conn.close()

    def get_all_cases(self):
        """Retrieve all cases from the database."""
        conn = None
        try:
            conn = self.get_connection()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM cases ORDER BY timestamp DESC')
            cases = [dict(row) for row in cursor.fetchall()]
            return cases
        except sqlite3.Error as e:
            print(f"Error retrieving cases: {e}")
            return []
        finally:
            if conn:
                conn.close()

    def get_case(self, case_number):
        """Retrieve a specific case by case number."""
        conn = None
        try:
            conn = self.get_connection()
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM cases WHERE case_number = ?', (case_number,))
            row = cursor.fetchone()
            if row:
                return dict(row)
            return None
        except sqlite3.Error as e:
            print(f"Error retrieving case: {e}")
            return None
        finally:
            if conn:
                conn.close()
