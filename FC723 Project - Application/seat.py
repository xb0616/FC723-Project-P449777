class Seat:
    # This class represents an individual seat on the airplane
    def __init__(self, seat_id, status='F',booking_ref=None):
        self.seat_id = seat_id  # Seat identifier (e.g., '12A')
        self.status = status    # 'F': Free, ref: Reserved, 'X': Aisle, 'S': Storage
        self.booking_ref = booking_ref

    def is_available(self):
        return self.status == 'F'

    def is_reserved(self):
        return self.status not in ['F', 'X', 'S']

    def book(self,ref):
        # Book the seat if it is free
        if self.is_available():
            self.status = ref
            self.booking_ref = ref
            return True
        return False

    def free(self):
        # Free the seat if it is reserved
        if self.is_reserved():
            self.status = 'F'
            self.booking_ref = None
            return True
        return False