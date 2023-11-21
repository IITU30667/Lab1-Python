class Episode:
    def __init__(self, id, name, air_date, episode, characters, url, created):
        self.id = id
        self.name = name
        self.air_date = air_date
        self.episode = episode
        self.characters = characters
        self.url = url
        self.created = created
        
    def display_info(self):
        return f"Episode: {self.name}, Air Date: {self.air_date}, Code: {self.episode}"

    def list_characters(self):
        return self.characters