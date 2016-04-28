import logging, players, wizard

class Core:
    '''
    Main class that serves as the transition platform and exchange point between
    all others.
    '''

    def __init__(self):
        '''
        (None) -> None

        Initial class creation. Without connection to infrastructure.
        '''
        self.gate = None
        self.db = None
        self.sessions = []
        self.wizards = []
        self.players = []
        logging.debug('Core is ready')

        return None

    def build_connections(self, infra):
        '''
        (list) -> None

        Creates connection to all infrastructure classes.
        '''
        self.gate = infra['gate']
        self.db = infra['database']
        logging.debug('Core connections are established')
        return None

    def start_session(self,wizard):
        '''
        (Wizard) -> None

        Creates session upon passed wizrd parameters.
        '''
        pass

    def add_player(self, id):
        '''
        (int) -> Wizard

        Creates player in core list with passed id. Creates Wizard for
        this player and returns this wizard instance.
        '''
        new_player = players.player(id)
        self.players.append(new_player)
        new_wiz = wizard.Wizard(new_player)
        self.wizards.append(new_wiz)
        return new_wiz

    def get_session_by_player(self,id):
        '''
        (int) -> Session

        Returns session that player with passed ID participates.
        In case is player does not exists - returns false.
        '''
        for player in self.players:
            if player.id == id:
                return player.session
        else:
            False



    def status(self):
        return "started"