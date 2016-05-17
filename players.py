class Player:

    def __init__(self, id):
        '''
        (list) -> None

        Initial class creation.
        '''
        self.id = id
        self.session = None # Session/Wizard that player is connected to
        self.population = []
        self.resources = []
        self.skills = {}
        self.infra = []     # Locations inside tribe territory and their state
        self.farm = []      # Tribe farm fields
        self.idle_turns = 0 # Number of turns that player was idle
                            # during allocation phase

        return None

    def set_session(self, session):
        self.session = session

    def get_man_by_name(self, name):
        '''

        '''
        for man in self.population:
            if name == man.name:
                return man
        return False

    def free_men(self):
        '''

        '''
        free_men = 0
        for man in self.population:
            if not man.is_allocated:
                free_men += 1
        return free_men

    def data(self):
        return {'population':[man.status() for man in self.population],
                'resources':self.resources,
                'skills':self.skills,
                'infra':[location.status() for location in self.infra],
                'farm':[farm.status() for farm in self.farm]
                }
