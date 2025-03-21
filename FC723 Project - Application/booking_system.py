from airplane import Airplane
import sys

class BookingSystem:
    # This class controls the user interface and seat booking logic
    def __init__(self):
        self.airplane = Airplane()

    def run(self):
        # Display the main menu and handle user input
        while True:
            print("\n--- Apache Airlines Seat Booking Menu ---")
            print("1. Check availability of seat")
            print("2. Book a seat")
            print("3. Free a seat")
            print("4. Show booking status")
            print("5. Exit program")
            choice = input("Enter your choice (1-5): ")

            if choice == '1':
                self.check_availability()
            elif choice == '2':
                self.book_seat()
            elif choice == '3':
                self.free_seat()
            elif choice == '4':
                self.show_booking_status()
            elif choice == '5':
                print("Exiting program. Goodbye!")
                sys.exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

    def check_availability(self):
        # Check the availability of a seat
        seat_id = input("Enter seat number (e.g., 12A): ").upper()
        seat = self.airplane.get_seat(seat_id)
        if seat:
            if seat.status == 'F':
                print(f"Seat {seat_id} is available.")
            elif seat.status == 'R':
                print(f"Seat {seat_id} is already reserved.")
            elif seat.status == 'X':
                print(f"Seat {seat_id} is an aisle and cannot be reserved.")
            elif seat.status == 'S':
                print(f"Seat {seat_id} is a storage area and cannot be reserved.")
        else:
            print("Invalid seat number.")

    def book_seat(self):
        # Book a seat if available
        seat_id = input("Enter seat number to book: ").upper()
        seat = self.airplane.get_seat(seat_id)
        if seat and seat.book():
            print(f"Seat {seat_id} has been successfully booked.")
        else:
            print(f"Cannot book seat {seat_id}. It may already be reserved or unavailable.")

    def free_seat(self):
        # Free a seat if it is currently reserved
        seat_id = input("Enter seat number to free: ").upper()
        seat = self.airplane.get_seat(seat_id)
        if seat and seat.free():
            print(f"Seat {seat_id} has been successfully freed.")
        else:
            print(f"Cannot free seat {seat_id}. It may not be reserved or is invalid.")

    def show_booking_status(self):
        # Display the current seating status chart
        self.airplane.display_seating()