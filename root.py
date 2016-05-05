from subprocess import Popen
import logging, players, wizard,os

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
        self.sessions = []  # active sessions
        self.wizards = []   # wizards of active players
        self.players = []   # Active players
        self.requests = []  # Requests that sent to Elder
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
        if int(wiz.conditions['merge']) != wiz.id:
            master_wiz_id = int(wiz.conditions['merge'])
            master_wiz = self.get_instance_by_player(master_wiz_id)
            if 'Wizard' not in str(type(master_wiz)):
                logging.error("Wrong class is detected when Wizard expected")
            master_wiz.add_player(wiz.players[0])
            self.wizards.remove(wiz)
        elif int(wiz.conditions['players']) > len(wiz.players):
            for i in range(0,int(wiz.conditions['players']) > len(wiz.players)):
                new_ai = self.db.get_free_ai()
                if new_ai:
                    print(new_ai,self.requests)
                    self.requests.append({'add_bot':new_ai,})
                    print(self.requests)

        return None


    def update(self):
        '''
        (None) -> None

        Updates all session and wizard instances.
        '''
        for wiz in self.wizards:
            if wiz.conditions['state'] == 'ready':
                self.update_wizard(wiz)
        pass
        '''
        for session in self.sessions:
            pass
        '''
        for request in self.requests:
            if 'add_bot' in request and self.get_instance_by_player(request['add_bot']['id']):
                self.requests.remove(request)

        return self.requests
