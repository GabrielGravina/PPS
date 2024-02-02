class TV:
    def __init__(self):
        self.turned_on = False
        self.volume = 0
        self.input = "HDMI1"
        
    def turn_on(self):
        print("TV is ON")
        self.turned_on = True

    def turn_off(self):
        print("TV is OFF")
        self.turned_off = False

    def set_input(self, input_source):
        print(f"TV input set to {input_source}")

class SurroundSoundSystem:
    def __init__(self):
        self.turned_on = False

    def turn_on(self):
        self.turned_on = True
        print("Surround Sound System is ON")

    def turn_off(self):
        self.turned_on = False
        print("Surround Sound System is OFF")

    def set_input(self, input_source):
        print(f"Surround Sound System input set to {input_source}")

    def set_volume(self, volume_level):
        print(f"Surround Sound System volume set to {volume_level}")

    def set_mode(self, mode):
        print(f"Surround Sound System mode set to {mode}")

class DVDPlayer:
    def __init__(self):
        self.turned_on = False
        
    def turn_on(self):
        self.turned_on = True
        print("DVD Player is ON")

    def turn_off(self):
        self.turned_on = False
        print("DVD Player is OFF")

    def play(self):
        print("DVD Player is playing")

    def stop(self):
        print("DVD Player stopped")

class CableTuner:
    def turn_on(self):
        print("Cable Tuner is ON")

    def turn_off(self):
        print("Cable Tuner is OFF")

    def set_channel(self, channel):
        print(f"Cable Tuner channel set to {channel}")

class EnterteinmentFacade:
    def __init__(self, tv, sound_system, dvd_player, cable_tuner):
        self.tv = tv
        self.sound_system = sound_system
        self.dvd_player = dvd_player
        self.cable_tuner = cable_tuner

    def watch_movie(self):
        self.tv.turn_on()
        self.sound_system.turn_on()
        self.dvd_player.turn_on()
        self.dvd_player.play()

    def listen_to_music(self):
        self.sound_system.turn_on()
        self.sound_system.set_mode("Stereo")

    def watch_cable_tv(self, channel):
        print(f"Turning TV on channel {channel}")
        self.tv.turn_on()
        self.input = 'HDMI1'
        self.cable_tuner.turn_on()
        self.cable_tuner.set_channel(channel)

    def turn_off_all(self):
        print("Turning off...")
        self.tv.turn_off()
        self.sound_system.turn_off()
        self.dvd_player.turn_off()
        self.cable_tuner.turn_off()


if __name__ == "__main__":
    tv = TV()
    sound_system = SurroundSoundSystem()
    dvd_player = DVDPlayer()
    cable_tuner = CableTuner()

    enterteinement_system = EnterteinmentFacade(tv, sound_system, dvd_player, cable_tuner)

    enterteinement_system.watch_movie()
    print("\n")

    enterteinement_system.listen_to_music()
    print("\n")

    enterteinement_system.watch_cable_tv(3)
    print("\n")

    enterteinement_system.turn_off_all()
