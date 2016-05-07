class player:

    def __init__(self, id):
        '''
        (list) -> None

        Initial class creation.
        '''
        self.id = id
        self.session = None # Session/Wizard that player is connected to
        self.population = []
        self.resources = []
        self.skills = []
        self.infra = None   # Locations inside tribe territory and their state
        self.farm = []      # Tribe farm fields

        return None

    def set_session(self, session):
        self.session = session