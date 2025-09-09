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
