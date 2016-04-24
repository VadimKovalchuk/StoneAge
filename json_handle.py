from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
import root
# @dispatcher.add_method
# def foobar(**kwargs):
#     return kwargs["foo"] + kwargs["bar"]

class Gate:

    #Singletone declaration
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Gate, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    #Singletone declaration is finished

    def __init__(self):
        self.core = None
        self.wizards = []
        self.players = {}
        print(self)

        return None

    def build_connections(self):
        self.core = root.Core()
        return None

    def allocation_command(self,strin):
        session = self.core.get_session_by_player(id)
        return str(session) + str(strin)

    def player_connect(self,id):
        session = self.core.get_session_by_player(id)
        return str(session)

    @Request.application
    def application(self,request):
        # Dispatcher is dictionary {<method_name>: callable}
        dispatcher["connect"] = self.player_connect
        dispatcher["allocate"] = self.allocation_command

        response = JSONRPCResponseManager.handle(
            request.data, dispatcher)
        print(request.data,'\n',response.data)
        return Response(response.json, mimetype='application/json')


    def start(self):
        run_simple('localhost', 4000, self.application)