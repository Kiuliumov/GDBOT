import sqlite3


def create_table():
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS users(
        discord_id TEXT PRIMARY KEY,
        username VARCHAR(255),
        password VARCHAR(255)
        )
        """
    )


def insert_user(discord_id, username, password):
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    cur.execute("""
    INSERT INTO users (discord_id, username, password) IF NOT EXISTS
    VALUES (%, % , %) 
    """, (discord_id, username, password))

    con.close()

def fetch_user(discord_id) -> dict[str:str]:
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM users WHERE discord_id = %
    """, discord_id)

    if cur.rowcount == 0:
        return None

    username, password = cur.fetchone()
    return {'username' : username, 'password': password}

def delete_user(discord_id):
    con = sqlite3.connect('users.db')
    cur = con.cursor()
    cur.execute("""
    DELETE FROM users WHERE discord_id = %
    """, discord_id)