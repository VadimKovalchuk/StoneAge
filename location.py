class Location:

    def __init__(self, location_data):
        '''
        (list) -> None

        Initial class creation. .
        '''
        self.name = location_data['name']
        self.type = location_data['type'] #Standard/private/quest/event
        self.description = location_data['description']
        self.full_fill = True if location_data['full_fill'] == 1 else False
        self.slots = [None for i in range(location_data['slots'])]

    def free_slots_amount(self):
        '''

        '''
        slots = 0
        for slot in self.slots:
            if slot is None:
                slots += 1
        return slots


    def allocate_man(self,man):
        '''

        '''
        if man.is_allocated:
            return False
        for i in range(len(self.slots)):
            if self.slots[i] is None:
                self.slots[i] = man
                return True
        return False


    def status(self):
        status = {'name':self.name,
                  'slots':[]}
        for man in self.slots:
            if man:
                status['slots'].append(man.map_status())
            else:
                status['slots'].append(None)
        return status
