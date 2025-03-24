import sqlite3

def init_db():
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS bookings (
                    booking_ref TEXT PRIMARY KEY,
                    passport_no TEXT,
                    first_name TEXT,
                    last_name TEXT,
                    seat_id TEXT
                )''')
    conn.commit()
    conn.close()

def insert_booking(booking_ref, passport_no, first_name, last_name, seat_id):
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("INSERT INTO bookings VALUES (?, ?, ?, ?, ?)",
              (booking_ref, passport_no, first_name, last_name, seat_id))
    conn.commit()
    conn.close()

def delete_booking(seat_id):
    conn = sqlite3.connect("bookings.db")
    c = conn.cursor()
    c.execute("DELETE FROM bookings WHERE seat_id = ?", (seat_id,))
    conn.commit()
    conn.close()
