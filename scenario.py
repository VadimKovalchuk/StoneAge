import location

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

        self.raw_map = {'forest':{}, 'stone':{}, 'clay':{}, 'hunting grounds':{},
                    'mother goddess':{},'public workshop':{}}
        self._create_map()

    def _create_map(self):
        for location_name in self.raw_map:
            location_data =  self.db.location_data(location_name)
            location_data.update(self.raw_map[location_name])
            location_data['name'] = location_name
            location_class = location.Location(location_data)
            self.session.map.append(location_class)

    def update_map(self):
        '''

        '''
        pass