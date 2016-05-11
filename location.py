class Session:

    def __init__(self, location_data):
        '''
        (list) -> None

        Initial class creation. .
        '''
        self.name = location_data['name']
        self.type = 'standard' #Standard/private/quest/event
        self.description = ''
        self.slots = []