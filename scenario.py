class Session:

    def __init__(self, name, db):
        '''
        (str, Database) -> None

        Initial class creation. Gets parameters and players from wizard.
        Makes self as the players session.
        '''
        self.name = name
        self.db = db