class Session:

    def __init__(self, wzrd):
        '''
        (list) -> None

        Initial class creation. Gets parameters and players from wizard.
        Makes self as the players session.
        '''
        self.id = wzrd.id
        self.players = wzrd.players
        self.rules = None       # TBD
        self.map = []           # TBD
        self.scenario = None    # TBD
        self.phase = 'allocation'  # Allocation/Day/Evening/Night
        self.log = {player: [] for player in self.players}  # Game events
                                            # that will be show to player

        for player in self.players:
            player.set_session(self)

        return None

    def set_status(self, player_id):
        pass

    def status(self):
        return 'session'