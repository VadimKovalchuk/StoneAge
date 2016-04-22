class Core:
    '''
    Main class that serves as the transition platform and exchange point between
    all others.
    '''

    #Singletone declaration
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Core, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    #Singletone declaration is finished

    def __init__(self):
        '''
        (list) -> None

        Initial class creation.
        '''
        self.sessions = []
        self.wizards = []
        self.players = {}
        print("Init core")

        return None

    def status(self):
        return "started"