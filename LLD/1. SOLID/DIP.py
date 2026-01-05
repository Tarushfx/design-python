# High-level module depends on specific database implementation
class OrderService:
    def __init__(self):
        self.db = Database()

    def place_order(self, order):
        self.db.save_order(order)


# Database implementation is hardcoded
class Database:
    def save_order(self, order):
        # Specific implementation to save order in database
        pass


# High-level module depends on an abstraction (interface)
class OrderService:
    def __init__(self, database):
        self.database = database

    def place_order(self, order):
        self.database.save_order(order)


# Interface defines the required behavior
class Database:
    def save_order(self, order):
        pass


# Different implementations of the interface
class MySQLDatabase(Database):
    # Specific implementation for MySQL database
    pass


class MongoDBDatabase(Database):
    # Specific implementation for MongoDB database
    pass


# Inject desired implementation at runtime
service = OrderService(MySQLDatabase())  # Or MongoDBDatabase()
# service.place_order(order)
