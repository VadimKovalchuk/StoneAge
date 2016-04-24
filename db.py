import json_handle, root

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
        print(self)

        return None

    def build_connections(self, infra):
        self.core = infra['core']
        self.gate = infra['gate']

        return None