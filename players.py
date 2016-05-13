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
        self.infra = []   # Locations inside tribe territory and their state
        self.farm = []      # Tribe farm fields

        return None

    def set_session(self, session):
        self.session = session

    def data(self):
        return {'population':[man.status() for man in self.population],
                'resources':self.resources,
                'skills':self.skills,
                'infra':[location.status() for location in self.infra],
                'farm':[farm.status() for farm in self.farm]
                }
