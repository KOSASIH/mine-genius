import numpy as np

class Aerospace:
    def __init__(self, spacecraft_type):
        self.spacecraft_type = spacecraft_type
        self.position = np.zeros((3,))
        self.velocity = np.zeros((3,))
        self.acceleration = np.zeros((3,))

    def simulate_orbit(self, time_step):
        # simulates the orbit of a spacecraft
        pass

    def simulate_reentry(self, time_step):
        # simulates the reentry of a spacecraft
        pass

    def simulate_landing(self, time_step):
        # simulates the landing of a spacecraft
        pass
