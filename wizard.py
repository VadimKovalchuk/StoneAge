class Wizard:

    def __init__(self, initial_player):
        '''
        (list) -> None

        Initial class creation.
        '''
        self.players = [initial_player]
        self.demands = {}

        self.players[0].set_session(self)

        return None