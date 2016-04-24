import json_handle
import players
import wizard

class Core:
    '''
    Main class that serves as the transition platform and exchange point between
    all others.
    '''

    #Singletone declaration
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Core, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    #Singletone declaration is finished

    def __init__(self):
        '''
        (list) -> None

        Initial class creation. Without connection to infrastructure.
        '''
        self.gate = None
        self.sessions = []
        self.wizards = []
        self.players = []
        print(self)

        return None

    def build_connections(self):
        self.gate = json_handle.Gate()

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