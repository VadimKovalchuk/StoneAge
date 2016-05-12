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
        self.map = []
        self.scenario = scenario.Scenario(wzrd.conditions['scenario'],self,self.db)
        self.phase = 'allocation'  # Allocation/Day/Evening/Night
        self.log = {player.id: [] for player in self.players}  # Game events
                                            # that will be show to player

        for player in self.players:
            player.set_session(self)
        self.scenario.initial_setup()

        return None

    def set_status(self, player_id):
        pass


    def status(self):
        status = {'phase': self.phase,'map':[]}
        for location in self.map:
            status['map'].append(location.status())
        return status