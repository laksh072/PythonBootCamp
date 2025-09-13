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

import os

class IncorrectFlightNumber(Exception):
    pass


class InsufficientSeats(Exception):
    pass


def read_flight_data(filename):
    flights = {} # dictionary to store flight infor
    file = None
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split()
                if len(parts) == 3:
                    flight_number, seats, price = parts[0], int(parts[1]), float(parts[2])
                    flights[flight_number] = {
                        "available_seats": seats,
                        "price_per_ticket": price,
                    }
        print(flights)
    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if not file:
            file.close()
    return flights


def book_tickets(flights, flight_number, num_tickets):

    if num_tickets <=0:
        raise ValueError("Number of tickets must be integers.")

    if flight_number not in flights:
        raise IncorrectFlightNumber(f"Flight {flight_number} not found.")

    flight = flights[flight_number]

    if num_tickets > flight["available_seats"]:
        raise InsufficientSeats(
            f"Only {flight['available_seats']} seats available, but {num_tickets} requested."
        )
    elif num_tickets <= 0:
        raise ZeroDivisionError("Number of tickets must be greater than zero.")

    total_cost = num_tickets * flight["price_per_ticket"]
    discount_onCost = total_cost * 0.3 # 30% discount

    # Update available seats
    flight["available_seats"] -= num_tickets

    return total_cost, discount_onCost

current_dir = os.getcwd()
abs_path = os.path.abspath(os.path.join(current_dir,"flightInfo.txt"))
flights = read_flight_data(abs_path)

try:
    flight_number = input("Enter flight number: ")
    num_tickets = int(input("Enter number of tickets to book: "))
    print(f"requesting {num_tickets} with flight {flight_number}")
    try:
        total_cost, discount_price = book_tickets(
            flights, flight_number, num_tickets
        )
        print(f"Flight {flight_number} booked successfully!")
        print(f"Total booking cost: {total_cost}")
        print(f"Discounted Price: {discount_price}")
    except IncorrectFlightNumber as fnfe:
        print(fnfe)
    except InsufficientSeats as sue:
        print(sue)
    except ValueError:
        print("Invalid input. Please enter numeric values for number of tickets.")
    except ZeroDivisionError:
        print("Number of tickets cannot be zero.")
finally:
    print("Thank you for using the Flight Management System.")
