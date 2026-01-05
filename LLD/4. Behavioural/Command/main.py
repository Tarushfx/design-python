# Command Interface
class Command:
    def execute(self):
        pass


# Concrete Commands
class PowerOnCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.power_on()


class VolumeUpCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.volume_up()


class ChannelUpCommand(Command):
    def __init__(self, tv):
        self.tv = tv

    def execute(self):
        self.tv.channel_up()


# Receiver
class TV:
    def power_on(self):
        print("TV is powered on")

    def volume_up(self):
        print("Volume increased")

    def channel_up(self):
        print("Channel changed")


# Invoker
class RemoteControl:
    def __init__(self):
        self.command = None

    def set_command(self, command):
        self.command = command
        return self

    def press_button(self):
        self.command.execute()


tv = TV()
remote = RemoteControl()

power_on = PowerOnCommand(tv)
volume_up = VolumeUpCommand(tv)
channel_up = ChannelUpCommand(tv)

remote.set_command(power_on).press_button()

remote.set_command(volume_up).press_button()

remote.set_command(channel_up).press_button()
