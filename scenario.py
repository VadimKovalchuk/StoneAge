import location, man

class Scenario:

    def __init__(self, name, session, db):
        '''
        (str, Database) -> None

        Initial class creation. Gets parameters and players from wizard.
        Makes self as the players session.
        '''
        self.name = name
        self.session = session
        self.db = db

        return None

    def _create_map(self):
        raw_map = {'forest':{},
                   'stone':{},
                   'clay':{},
                   'hunting grounds':{},
                   'mother goddess':{},
                   'public workshop':{}
                   }

        for location_name in raw_map:
            location_data =  self.db.location_data(location_name)
            location_data.update(raw_map[location_name])
            location_data['name'] = location_name
            location_class = location.Location(location_data)
            self.session.map.append(location_class)
        return None

    def _starting_population(self):
        '''

        '''
        for player in self.session.players:
            player.population = [man.Man(player.id) for i in range(5)]

    def initial_setup(self):
        '''

        '''
        self._create_map()
        self._starting_population()

        return None

    def update_map(self):
        '''

        '''
        pass