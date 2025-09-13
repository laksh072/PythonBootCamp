# 3. Create a base class Service, and derive two classes: SecurityService and BaggageService.

# Requirements:
# -Service class has a method service_info().
# -Derived classes override or extend this to describe their own service.
 
class Service:
    def service_info(self):
        return "Base class service."

class SecurityService(Service):
    def service_info(self):
        return "SecurityService class service."

class BaggageService(Service):
    def service_info(self):
        return "BaggageService class service."

base_service = Service()
security_service = SecurityService()
baggage_service = BaggageService()


print(base_service.service_info())
print(security_service.service_info())
print(baggage_service.service_info())
