from abc import ABC, abstractmethod


class Device(ABC):
    _volume = 0
    on = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def set_volume(self, volume):
        self._volume = volume
        print(f"Current volume: {self._volume}")

    def get_volume(self):
        # print(f"Current volume: {self._volume}")
        return self._volume


class TV(Device):
    def __init__(self):
        super().__init__()
        self.channel = 1

    def turn_on(self):
        self.on = True
        print(f"TV turned on (channel: {self.channel})")

    def turn_off(self):
        self.on = False
        print("TV turned off")

    def change_channel(self, channel):
        self.channel = channel
        print(f"Switched to channel {channel}")


class Stereo(Device):
    def __init__(self):
        super().__init__()

    def turn_on(self):
        self.on = True
        print("Stereo turned on")

    def turn_off(self):
        self.on = False
        print("Stereo turned off")

    def set_volume(self, volume):
        self.volume = volume
        print(f"Stereo volume set to {volume}")


class RemoteControl:
    def __init__(self, device: Device):
        self.device = device

    def button_clicked(self, button):
        if button == "Power":
            if self.device.on:
                self.device.turn_off()
            else:
                self.device.turn_on()
        elif button == "VolumeUp":
            self.device.set_volume(self.device.get_volume() + 1)
        elif button == "VolumeDown":
            self.device.set_volume(self.device.get_volume() - 1)
        elif button == "ChannelUp" and isinstance(self.device, TV):
            self.device.change_channel(self.device.channel + 1)
        elif button == "ChannelDown" and isinstance(self.device, TV):
            self.device.change_channel(self.device.channel - 1)
        else:
            print(f"Unknown button: {button}")


tv = TV()
remote = RemoteControl(tv)

remote.button_clicked("Power")
remote.button_clicked("VolumeUp")
remote.button_clicked("VolumeUp")
remote.button_clicked("ChannelUp")
remote.button_clicked("Power")

stereo = Stereo()
stereo_remote = RemoteControl(stereo)
stereo_remote.button_clicked("Power")
stereo_remote.button_clicked("VolumeUp")
stereo_remote.button_clicked("Power")
