import logging, sqlite3, time

ai_creation_timeout = 1

class Database:
    '''
    .
    '''

    def __init__(self):
        '''
        (list) -> None

        Initial class creation. Without connection to infrastructure.
        '''
        self.core = None
        self.gate = None
        self.db = sqlite3.connect('database/general.db')
        self.db_cursor = self.db.cursor()
        self.timestamp = time.time()

        logging.debug('Database is ready')
        return None

    def build_connections(self, infra):
        self.core = infra['core']
        self.gate = infra['gate']
        logging.debug('Database connections are established')
        return None

    def player_login(self, login, password):
        '''
        (None) -> bool

        Validates player credentials.
        '''
        query = 'SELECT id, pass FROM players WHERE login is "' + login +'"'
        self.db_cursor.execute(query)
        row = self.db_cursor.fetchone()
        player_id,db_pass = row
        if db_pass == password:
            return player_id

    def get_free_ai(self):
        '''

        '''
        a = time.time() - self.timestamp
        if time.time() - self.timestamp < ai_creation_timeout:
            return False
        self.timestamp = time.time()
        query = 'SELECT id, login, pass FROM players WHERE ai is "1"'
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        for row in rows:
            id, login, pas = row
            if not self.core.get_instance_by_player(int(id)):
                return {'login': login, 'pass': pas}

        return False