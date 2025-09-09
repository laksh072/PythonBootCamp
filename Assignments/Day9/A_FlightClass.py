class Flight:

    def __init__(self, flightName, flightNo):
        self.Name = flightName
        self.Number = flightNo

    def display_Flight_Info(self):
        print(f"{self.Name} : {self.Number}")

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