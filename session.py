class session:

    def __init__(self, id):
        '''
        (list) -> None

        Initial class creation.
        '''
        self.id = id
        self.session = None

        return True

    def set_session(self, session):
        self.session = session