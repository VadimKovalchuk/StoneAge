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

    def get_instance_by_player(self,id):
        '''
        (int) -> Session

        Returns session/wizard that player with passed ID bind to.
        In case if player does not exists - returns false.
        '''
        for player in self.players:
            if player.id == id:
                return player.session
        else:
            False

    def update_wizard(self, wiz):
        '''
        (Wizard) -> None

        Updates passed wizard instance according to condition parameters.
        '''
        if 'merge' in wiz.conditions:
            master_wiz_id = wiz.conditions['merge']
            master_wiz = self.get_instance_by_player(master_wiz_id)
            if type(master_wiz) != type(wizard.Wizard):
                logging.error("Wrong class is detected when Wizard expected")
            master_wiz.add_player(wiz.players[0])
            self.wizards.remove(wiz)
        elif wiz.conditions['players'] > len(wiz.players):
            ia_amount = wiz.conditions['players'] - len(wiz.players)
            # self.create_ai(ai_amount,wiz.id)


    def update(self):
        '''
        (None) -> None

        Updates all session and wizard instances.
        '''
        for wiz in self.wizards:
            if wiz.conditions['state'] == 'ready':
                self.update_wizard(wiz)
        return None


    def status(self):
        return "started"