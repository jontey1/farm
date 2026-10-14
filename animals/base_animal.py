
class BaseAnimal:
    def __init__(self, name, noise):
        self.name = name
        self.noise = noise

    def make_noise(self):
        print(self.noise)
        raise NotImplementedError("Subclasses must implement make_noise method")

