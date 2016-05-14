import location, man

start_pop_amount = 5

names = ["Oku", "Buba", "Cora", "Garu", "Okupa", "Timb", "Dema", "Hala",
                 "Kibo", "Moz", "Zev", "Aka", "Lem", "Nurg", "Pela"]

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
                   'hunting_grounds':{},
                   'mother_goddess':{},
                   'public_workshop':{},
                   'trade_shop':{},
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
            player.population = [man.Man(player.id,names[i]) \
                                 for i in range(start_pop_amount)]
        return None

    def _initial_infra(self):
        '''

        '''
        raw_infra = {'campfire':{},
                     'farm':{}}
        for player in self.session.players:
            for location_name in raw_infra:
                location_data =  self.db.location_data(location_name)
                location_data.update(raw_infra[location_name])
                location_data['name'] = location_name
                location_class = location.Location(location_data)
                if location_class.type == 'farm':
                    player.farm.append(location_class)
                else:
                    player.infra.append(location_class)

        return None

    def initial_setup(self):
        '''

        '''
        self._create_map()
        self._starting_population()
        self._initial_infra()

        return None

    def update_map(self):
        '''

        '''
        pass