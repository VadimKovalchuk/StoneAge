class Wizard:

    def __init__(self, initial_player):
        '''
        (list) -> None

        Initial class creation.
        '''
        self.id = initial_player.id
        self.players = [initial_player]
        self.rules = {'mode': 'single',
                      'players':4,
                      'map':'default'}

        self.players[0].set_session(self)

        return None

    def status(self):
        '''
        (None) -> Dict
        '''
        print('status:')
        result = self.rules.copy()
        print(result)
        result['wizard_id']= self.id
        print(result)
        return result


    def add_player(self, new_player):
        '''
        (Player) -> None

        Adds passed player to curent players list and replaces his
        active session to self.
        '''
        self.players.append(new_player)
        new_player.set_session(self)

        return None
