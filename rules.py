from random import randint

class Rules:

    def __init__(self, session):
        '''
        (Sesssion) -> None

        Initial class creation.
        '''
        self.session = session

        return None

    def process_day_phase(self):
        '''
        (None) -> TBD

        Performs day phase actions.
        '''
        result = {player.id: {} for player in self.session.players}
        locations = []
        locations.extend(self.session.map)
        for player in self.session.players:
            locations.extend(player.infra)
            locations.extend(player.farm)

        for location in locations:
            for man in location.slots:
                if not man:
                    continue
                if location.name not in result[man.player]:
                    result[man.player][location.name] = {}
                dice_result = randint(1,man.points)
                result[man.player][location.name][man.name] = dice_result
                #man.is_allocated = False



        return result
