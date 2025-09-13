# 1. Create a base class Flight with basic flight information. Create a derived class ScheduledFlight that adds scheduling information.

# Requirements:
# -Flight should have attributes: flight number, airline.
# -ScheduledFlight should add departure time and arrival time.
# -Include methods to display complete flight information.

class Flight:

    def __init__(self, flightName, flightNo):
        self.Name = flightName
        self.Number = flightNo

    def display_Flight_Info(self):
        print(f"FlightInfo - {self.Name} : {self.Number}")

class ScheduledFlight(Flight):

    def __init__(self, flightName, flightNo, departure, arrival):
        super().__init__(flightName, flightNo)
        self.arrival = arrival
        self.departure = departure
    
    def display_Scheduled_Flight_Info(self):
        self.display_Flight_Info()
        print(f"From {self.departure} to {self.arrival} ")

sf = ScheduledFlight("Boeing", "A123", "2300h","1015h")
sf.display_Scheduled_Flight_Info()