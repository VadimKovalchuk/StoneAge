from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
from jsonrpc import JSONRPCResponseManager, dispatcher
import session, logging
# @dispatcher.add_method
# def foobar(**kwargs):
#     return kwargs["foo"] + kwargs["bar"]

class Gate:

    def __init__(self):
        self.core = None
        self.db = None
        self.wizards = []
        self.players = {}
        logging.debug('Gate is ready')

        return None

    def build_connections(self,infra):
        self.core = infra['core']
        self.db = infra['database']
        logging.debug('Gate connections are established')
        return None

    def player_connect(self, login, password):
        player_id =self.db.player_login(login, password)
        current_session = self.core.get_instance_by_player(player_id)
        if(not current_session):
            current_session = self.core.add_player(player_id)
        return {'id':player_id,
                'session_type':str(type(current_session)),
                'session_id':current_session.id
                }

    def status(self, player_id):
        current_inst = self.core.get_instance_by_player(int(player_id))
        print(current_inst.status())
        if(current_inst):
            return current_inst.status()

    def allocation_command(self,strin):
        curent_session = self.core.get_session_by_player(id)
        if type(curent_session) != type(session.session):
            return False

        return True

    @Request.application
    def application(self,request):
        # Dispatcher is dictionary {<method_name>: callable}
        dispatcher["connect"] = self.player_connect
        dispatcher["status"] = self.status
        dispatcher["allocate"] = self.allocation_command


        response = JSONRPCResponseManager.handle(
            request.data, dispatcher)
        print(request.data,'\n',response.data)
        return Response(response.json, mimetype='application/json')


    def start(self):
        run_simple('localhost', 4000, self.application)