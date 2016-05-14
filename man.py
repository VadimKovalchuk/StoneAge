class Man:

    def __init__(self, player_id, name = ''):

        self.player = player_id
        self.alive = True
        self.name = name
        self.is_allocated = False
        self.points = 6
        self.weapon = None
        self.wear = None
        self.inventory = [None, None, None]

        return None

    def client_json(self,dict):
        '''

        '''
        self.alive = dict['alive']
        self.is_allocated = dict['is_allocated']
        self.points = dict['points']
        self.weapon = dict['weapon']
        self.wear = dict['wear']
        self.inventory = dict['inventory']

    def status(self):
        return self.__dict__

    def map_status(self):
        return {'name':self.name,'player':self.player}