import sqlite3
import json
import os

class PersistenceEngine:
    def __init__(self, db_path="config/vault.db"):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Creates the vault table if it doesn't exist."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS identities 
                          (app_id TEXT PRIMARY KEY, profile_json TEXT, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        conn.commit()
        conn.close()

    def save_identity(self, app_id, dna_profile):
        """Locks a DNA profile to a specific app instance."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        profile_data = json.dumps(dna_profile)
        cursor.execute("INSERT OR REPLACE INTO identities (app_id, profile_json) VALUES (?, ?)", (app_id, profile_data))
        conn.commit()
        conn.close()
        print(f"[VAULT] Identity locked for {app_id}.")

    def load_identity(self, app_id):
        """Retrieves the original DNA to prevent identity drift."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT profile_json FROM identities WHERE app_id=?", (app_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            print(f"[VAULT] Restoring original DNA for {app_id}...")
            return json.loads(row[0])
        return None
