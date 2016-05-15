import scenario, time

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
        self.log = []  # Game events that will be show to player
        self.round = 1
        self.points = {}
        self.first_turn = self.players[0]
        self.player_turn = self.players[0]
        self.turn_start_time = time.time()

        for player in self.players:
            player.set_session(self)

        self.scenario.initial_setup()

        return None

    def _get_player(self,player_id):
        '''

        '''
        for player in self.players:
            if player.id == player_id:
                return player
        return None

    def _get_location(self,location_name,player_id):

        for location in self.map:
            if location.name == location_name:
                return location
        player = self._get_player(player_id)

        if not player:
            return False

        for location in player.infra:
            if location.name == location_name:
                return location
        for location in player.farm:
            if location.name == location_name:
                return location
        return False

    def _next_player_turn(self):
        '''

        '''
        player_index = self.players.index(self.player_turn)
        player_index += 1
        if player_index == len(self.players):
            self.player_turn = self.players[0]
        else:
            self.player_turn = self.players[player_index]
        return None

    def _all_players_done(self):
        for player in self.players:
            if not player.is_all_allocated():
                return False
        return True


    def allocation(self, player_id, location_name, men):

        location = self._get_location(location_name, player_id)
        if not location:
            return False
        if location.type == 'standard' and \
           player_id != self.player_turn.id:
            return False
        if location.free_slots_amount() < len(men):
            return False
        if location.full_fill is True and \
            location.free_slots_amount() != len(men):
            return False
        player = self._get_player(player_id)
        for name in men:
            man = player.get_man_by_name(name)
            if not man:
                return False
            if location.allocate_man(man):
                man.is_allocated = True
            else:
                return False
        if player_id == self.player_turn.id:
            self._next_player_turn()

        return True




    def status(self):
        status = {'type': 'session',
                  'phase': self.phase,
                  'player_turn': self.player_turn.id,
                  'map':[]}
        for location in self.map:
            status['map'].append(location.status())
        return status