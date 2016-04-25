import logging, players, wizard

class Core:
    '''
    Main class that serves as the transition platform and exchange point between
    all others.
    '''

    def __init__(self):
        '''
        (list) -> None

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
        self.gate = infra['gate']
        self.db = infra['database']
        logging.debug('Core connections are established')
        return None

    def start_session(self,wizard):
        pass

    def get_session_by_player(self,id):
        for player in self.players:
            if player.id == id:
                return player.session
        else:
            new_player = players.player(id)
            self.players.append(new_player)
            new_wiz = wizard.Wizard(new_player)
            self.wizards.append(new_wiz)
            return new_wiz


    def status(self):
        return "started"