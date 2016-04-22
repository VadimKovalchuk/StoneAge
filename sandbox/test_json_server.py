from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import time

from jsonrpc import JSONRPCResponseManager, dispatcher



@dispatcher.add_method
def foobar(**kwargs):
    return kwargs["foo"] + kwargs["bar"]

def pussy(str1, str2):
    return {1:str1,2:str2}

@Request.application
def application(request):
    # Dispatcher is dictionary {<method_name>: callable}
    dispatcher["echo"] = lambda s: s
    dispatcher["add"] = lambda a, b: a + b
    dispatcher["pussy"] = pussy

    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    print(request.data,'\n',response.data)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 4000, application)
    while True:
        print("tick")
        time.sleep(1)