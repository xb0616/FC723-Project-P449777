from seat import Seat

class Airplane:
    # This class manages the entire airplane seating layout
    def __init__(self, rows=80, columns=['A','B','C','D','E','F']):
        self.rows = rows
        self.columns = columns
        self.seats = {}
        self.initialize_seats()

    def initialize_seats(self):
        # Create all seats and assign appropriate status
        for row in range(1, self.rows + 1):
            for col in self.columns:
                seat_id = f"{row}{col}"
                if col == 'D' and row > 76:
                    status = 'S'  # Storage area
                elif col in ['E', 'F'] and row > 76:
                    status = 'S'  # Storage area
                elif col == 'C' and row % 5 == 0:
                    status = 'X'  # Aisle
                else:
                    status = 'F'  # Free
                self.seats[seat_id] = Seat(seat_id, status)

    def get_seat(self, seat_id):
        return self.seats.get(seat_id)

    def display_seating(self):
        # Print the seating chart row by row
        print("\nCurrent Seating Status:")
        for row in range(1, self.rows + 1):
            row_status = []
            for col in self.columns:
                seat_id = f"{row}{col}"
                seat = self.get_seat(seat_id)
                if seat:
                    row_status.append(seat.status)
                else:
                    row_status.append(" ")
            print(f"Row {row:02}: {' '.join(row_status)}")