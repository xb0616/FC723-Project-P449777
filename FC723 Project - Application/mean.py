from booking_system import BookingSystem
from database import init_db

init_db()                 # initiate the database
system = BookingSystem()  # Create the booking system
system.run()              # Start the menu loop