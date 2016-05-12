class Location:

    def __init__(self, location_data):
        '''
        (list) -> None

        Initial class creation. .
        '''
        self.name = location_data['name']
        self.type = location_data['type'] #Standard/private/quest/event
        self.description = location_data['description']
        self.slots = [None for i in range(location_data['slots'])]

        return None

    def status(self):
        status = {'name':self.name,
                  'slots':self.slots}
        return status

