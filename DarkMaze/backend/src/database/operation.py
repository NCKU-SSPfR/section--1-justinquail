import sqlite3
import json

def create_user(username):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_state (username, current_level_name, map_size, health, path, current_position) VALUES (?, ?, ?, ?, ?, ?)",
                   (username, "maze-level-1", json.dumps([10, 10]), 3, json.dumps([]), json.dumps([1, 0])))
    conn.commit()
    conn.close()

def reset_game_state(username):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM game_state WHERE username = ?", (username,))
    conn.commit()
    conn.close()

def save_game_state(username, current_level_name, map_size, health, path, current_position):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_state (username, current_level_name, map_size, health, path, current_position) VALUES (?, ?, ?, ?, ?, ?)",
                   (username, current_level_name, json.dumps(map_size), health, json.dumps(path), json.dumps(current_position)))
    conn.commit()
    conn.close()

def get_latest_game_state(username):
    conn = sqlite3.connect("game.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game_state WHERE username = ? ORDER BY id DESC LIMIT 1", (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {
            "id": row[0],
            "username": row[1],
            "current_level_name": row[2],
            "map_size": json.loads(row[3]),
            "health": row[4],
            "path": json.loads(row[5]),
            "current_position": json.loads(row[6])
        }
    return None
