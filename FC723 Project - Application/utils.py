import random
import string

# Save all the reservation numbers that have been generated
generated_refs = set()

def generate_booking_reference():
    while True:
        ref = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
        if ref not in generated_refs:
            generated_refs.add(ref)
            return ref

