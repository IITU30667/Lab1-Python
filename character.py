class Character:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def display_basic_info(self):
        return f"Name: {self.name}, Status: {self.status}, Species: {self.species}"

    def list_episodes(self):
        return self.episode