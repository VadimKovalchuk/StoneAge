class Session:

    def __init__(self, name):
        '''
        (list) -> None

        Initial class creation. .
        '''
        self.name = name
        self.type = 'standard' #Standard/private/quest/event
        self.description = ''
        self.slots = []