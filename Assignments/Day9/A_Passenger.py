#multiple inheritance
# 4. Create one class PassengerDetails and another class TicketDetails. Create a new class Booking that inherits from both.

# Requirements:

# - PassengerDetails has name, age.
# - TicketDetails has ticket number, seat number.
# - Booking shows all information.

class Passenger:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Ticket:
    def __init__(self, ticket_number, seat_number):
        self.ticket_number = ticket_number
        self.seat_number = seat_number

class Booking(Passenger, Ticket):

    def __init__(self, name, age, ticket_number, seat_number):
        # super().__init__(name, age)
        # super().__init__(ticket_number, seat_number) -- super considers only the FIRST class passed for inheritance ie Passenger, 
        #even thou we have ticket also as parent class, hence access with class name
        Passenger.__init__(self,name, age)
        Ticket.__init__(self,ticket_number, seat_number)

    def display_booking_info(self):
        return (f"Passenger Name: {self.name}\n"
                f"Passenger Age: {self.age}\n"
                f"Ticket Number: {self.ticket_number}\n"
                f"Seat Number: {self.seat_number}")


booking = Booking("Lakshmi", 28, "TCK1111", "11A")
print(booking.display_booking_info())
