class ExpensiveService:
    def __init__(self):
        print("Creating ExpensiveService...")

    def perform_task(self):
        print("Performing expensive task...")


class ServiceProxy:
    def __init__(self):
        self.expensive_service = None
        self.has_access = False

    def grant_access(self):
        self.has_access = True

    def perform_task(self):
        if not self.has_access:
            print("Access denied. Please authenticate.")
            return
        if not self.expensive_service:
            self.expensive_service = ExpensiveService()

        self.expensive_service.perform_task()


# Usage
service_proxy = ServiceProxy()

# Initially, access is denied
service_proxy.perform_task()

# Grant access and then use the service
service_proxy.grant_access()
service_proxy.perform_task()
