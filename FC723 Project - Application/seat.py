class Seat:
    # This class represents an individual seat on the airplane
    def __init__(self, seat_id, status='F'):
        self.seat_id = seat_id  # Seat identifier (e.g., '12A')
        self.status = status    # 'F': Free, 'R': Reserved, 'X': Aisle, 'S': Storage

    def is_available(self):
        return self.status == 'F'

    def is_reserved(self):
        return self.status == 'R'

    def book(self):
        # Book the seat if it is free
        if self.is_available():
            self.status = 'R'
            return True
        return False

    def free(self):
        # Free the seat if it is reserved
        if self.is_reserved():
            self.status = 'F'
            return True
        return False