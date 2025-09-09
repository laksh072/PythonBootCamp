# Problem Statement
# You are asked to design a Flight Management System in Python using exception handling.
# The system should:
# - Read flight information from a file called flights.txt.
# - Each line has: flight_number available_seats price_per_ticket
#   Example: AI101 50 6000
# Ask the user for:
# - Flight number
# - Number of tickets to book
# Implement the following exception rules: (Questions below)
# (a) Raise FlightNotFoundError (custom) if the entered flight number does not exist.
# (b) Raise SeatsUnavailableError (custom) if requested tickets exceed available seats.
# (c) Handle ValueError if user enters invalid input (like string instead of integer).
# (d) Handle ZeroDivisionError if user enters 0 tickets (while calculating discount per ticket).
# (e) Always close the file using finally.
# The program should print:
# - Flight details
# - Total booking cost
# - Discount per ticket (total / tickets)
# Note:
# Use nested try-except:
# Inner block for booking operations.
# Outer block for file handling & re-raised exceptions


class FlightNotFoundError(Exception):
    pass


class SeatsUnavailableError(Exception):
    pass


def read_flight_data(filename):
    flights = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    flight_number = parts[0]
                    available_seats = int(parts[1])
                    price_per_ticket = float(parts[2])
                    flights[flight_number] = {
                        "available_seats": available_seats,
                        "price_per_ticket": price_per_ticket,
                    }
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return flights


def book_tickets(flights, flight_number, num_tickets):

    if num_tickets is not int:
        raise ValueError("Number of tickets must be integers.")

    if flight_number not in flights:
        raise FlightNotFoundError(f"Flight {flight_number} not found.")

    flight = flights[flight_number]

    if num_tickets > flight["available_seats"]:
        raise SeatsUnavailableError(
            f"Only {flight['available_seats']} seats available, but {num_tickets} requested."
        )
    elif num_tickets <= 0:
        raise ZeroDivisionError("Number of tickets must be greater than zero.")

    total_cost = num_tickets * flight["price_per_ticket"]
    discount_per_ticket = total_cost / num_tickets

    # Update available seats
    flight["available_seats"] -= num_tickets

    return total_cost, discount_per_ticket


filename = "flightInfo.txt"
flights = read_flight_data(filename)

try:
    flight_number = input("Enter flight number: ")
    num_tickets = int(input("Enter number of tickets to book: "))

    try:
        total_cost, discount_per_ticket = book_tickets(
            flights, flight_number, num_tickets
        )
        print(f"Flight {flight_number} booked successfully!")
        print(f"Total booking cost: {total_cost}")
        print(f"Discount per ticket: {discount_per_ticket}")
    except FlightNotFoundError as fnfe:
        print(fnfe)
    except SeatsUnavailableError as sue:
        print(sue)
    except ValueError:
        print("Invalid input. Please enter numeric values for number of tickets.")
    except ZeroDivisionError:
        print("Number of tickets cannot be zero.")
finally:
    print("Thank you for using the Flight Management System.")
