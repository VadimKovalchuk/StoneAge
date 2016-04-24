import json_handle, db
import players
import wizard

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
        print(self)

        return None

    def build_connections(self, infra):
        self.gate = infra['gate']
        self.db = infra['database']
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