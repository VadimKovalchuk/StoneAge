class Item:
    '''

    '''

    def __init__(self, id, item_type, name, expiry_term=999, modifier=None):
        '''
        (int, str, str, int, int) -> None

        Initial class creation with parameters assignment.
        '''
        self.id = id
        self.type = item_type  # resource, weapon, instrument, consumable, wear
        self.name = name
        self.expiry_term = expiry_term
        self.modifier = modifier
        self.icon = name

        return None

    def aging(self, amount=1):
        '''
        (int) -> None

        Decrease of expiry term for resorces or durability for items
        '''
        self.expiry_term -= amount
        return None

    def status(self):
        '''
        (None) -> dict

        Returns all item parameters.
        '''
        return self.__dict__

