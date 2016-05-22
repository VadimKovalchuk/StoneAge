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
        for location in self.session.map:
            if location.type == 'standard':
                for man in location.slots:
                    if not man:
                        continue
                    if location.name not in result[man.player]:
                        result[man.player][location.name] = {}
                    dice_result = randint(1,man.points)
                    result[man.player][location.name][man.name] = dice_result
                    #man.is_allocated = False

        for player in self.session.players:
            for farm in player.farm:
                for man in farm.slots:
                    if not man:
                        continue
                    if farm.name not in result[man.player]:
                        result[player.id][farm.name] = {}
                    dice_result = randint(1,man.points)
                    result[man.player][farm.name][man.name] = dice_result
                    #man.is_allocated = False

        for player in self.session.players:
            for building in player.infa:
                for man in building.slots:
                    if not man:
                        continue
                    if building.name not in result[man.player]:
                        result[player.id][building.name] = {}
                    dice_result = randint(1,man.points)
                    result[man.player][building.name][man.name] = dice_result
                    #man.is_allocated = False


        return result
