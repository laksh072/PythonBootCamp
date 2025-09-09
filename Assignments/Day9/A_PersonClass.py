#Multi level inheritance

class Person:

    def __init__(self,name,ssid):
        self.Name = name
        self.ID = ssid

    def display_Person_Info(self):
        print(f"{self.Name} - {self.ID}")

class CrewMember(Person):

    def __init__(self,name, ssid,role):
        super().__init__(name,ssid)
        self.Role = role

    def display_Crew_Info(self):
        self.display_Person_Info()
        print(self.Role)

class Pilot(CrewMember):

    def __init__(self,name,ssid,role,rank,licenseID):
        super().__init__(name,ssid,role)
        self.Rank = rank
        self.licenseID = licenseID
        
    def display_Pilot_Info(self):
        self.display_Crew_Info()
        print(self.Rank, " ",  self.licenseID )

pilot = Pilot("Raj","1111","Pilot","Captain","AW125")
pilot.display_Pilot_Info()