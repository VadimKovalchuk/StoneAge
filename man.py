class Man:

    def __init__(self, player_id):

        self.player = player_id
        self.alive = True
        self.name = ''
        self.is_allocated = False
        self.points = 6
        self.weapon = None
        self.wear = None
        self.inventory = [None, None, None]

        return None

    def status(self):
        return self.__dict__