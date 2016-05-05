import logging, sqlite3

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
        query = 'SELECT id, login, pass FROM players WHERE ai is "1"'
        self.db_cursor.execute(query)
        rows = self.db_cursor.fetchall()
        for row in rows:
            #bot_id, login, pas = row
            bot_id = row[0]
            login = row[1]
            pas = row[2]
            if not self.core.get_instance_by_player(id):
                return {'id':bot_id,'login': login, 'pass': pas}

        return False