import scenario

class Session:

    def __init__(self, wzrd, db):
        '''
        (list, Database) -> None

        Initial class creation. Gets parameters and players from wizard.
        Makes self as the players session.
        '''
        self.id = wzrd.id
        self.db = db
        self.players = wzrd.players
        self.rules = None       # TBD
        self.map = []           # TBD
        self.scenario = scenario.Scenario(wzrd.conditions['scenario'],self,self.db)
        self.phase = 'allocation'  # Allocation/Day/Evening/Night
        self.log = {player.id: [] for player in self.players}  # Game events
                                            # that will be show to player

        for player in self.players:
            player.set_session(self)


        return None

    def set_status(self, player_id):
        pass


    def status(self):
        status = {'map':{}}
        for location in self.map:
            status[map][location.name] = location.status()
        return status