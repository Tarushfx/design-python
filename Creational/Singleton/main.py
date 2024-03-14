class Singleton:
    _instance = None

    def __init__(self):
        if self._instance is not None:
            raise Exception(
                "Singleton instance already exists. Use getInstance() method instead."
            )

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


# Eager Loading
class SingletonEager:
    _instance = None
    ok = 3

    # @classmethod
    def __new__(cls, ok):
        # cls.ok = ok
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance


class SingletonLazy:
    _instance = None

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance


import threading


# Thread safety
class SingletonThreadSafe:
    _instance = None
    _lock = threading.Lock()

    @classmethod
    def getInstance(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance


if __name__ == "__main__":
    # Access the Singleton instance
    singleton1 = Singleton.getInstance()
    singleton2 = Singleton.getInstance()

    print(singleton1 is singleton2)  # Output: True
    singleton1 = SingletonLazy.getInstance()
    singleton2 = SingletonLazy.getInstance()

    print(singleton1 is singleton2)

    singleton2 = SingletonEager(2)
    print(singleton2.ok)
    singleton1 = SingletonEager(5)
    print(singleton1.ok)  # Output: True

    print(singleton1 is singleton2)  # Output: True
