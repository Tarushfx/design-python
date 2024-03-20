class Light:
    def __init__(self, room):
        self.room = room
        self.on = False

    def turn_on(self):
        self.on = True
        print(f"{self.room} light turned on")

    def turn_off(self):
        self.on = False
        print(f"{self.room} light turned off")


class Thermostat:
    def __init__(self):
        self.target_temp = 72

    def set_temperature(self, temp):
        self.target_temp = temp
        print(f"Thermostat set to {temp} degrees Fahrenheit")

    def get_temperature(self):
        return self.target_temp


class SecuritySystem:
    def __init__(self):
        self.armed = False

    def arm_system(self):
        self.armed = True
        print("Security system armed")

    def disarm_system(self):
        self.armed = False
        print("Security system disarmed")


class HomeAutomationFacade:
    def __init__(self):
        self.living_room_light = Light("Living Room")
        self.kitchen_light = Light("Kitchen")
        self.thermostat = Thermostat()
        self.security_system = SecuritySystem()

    def good_morning(self):
        self.living_room_light.turn_on()
        self.thermostat.set_temperature(72)

    def good_night(self):
        self.living_room_light.turn_off()
        self.thermostat.set_temperature(68)
        self.security_system.arm_system()


home_automation = HomeAutomationFacade()

home_automation.good_morning()
home_automation.good_night()

home_automation.kitchen_light.turn_on()
