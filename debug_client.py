import requests
import json

player = None

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}
command_args = {'connect':['login', 'password'],
                'status':[]}



def send_request(method,params,id):
    '''

    '''
    payload = {
            "method": method,
            "params": params,
            "jsonrpc": "2.0",
            "id": id,
        }
    response = requests.post(url,
                             data=json.dumps(payload),
                             headers=headers).json()
    assert response['id'] != str(id), 'Invalid ID is rescieved for connect request'

    return response

def get_command_arguments(name):
    '''

    '''
    if name in command_args:
        params = {}
        if len(command_args[name]) == 0:
            return {}
        for argument in command_args[name]:
            print(argument,': ',end='')
            value = input()
            params[argument] = value
        return params
    else:
        return False

def login_flow():
    '''

    '''
    response = None

    for attempt in range(1,4):
        args = get_command_arguments('connect')
        response = send_request('connect',args,0)
        assert response['id'] != str(0), 'Invalid ID is rescieved for connect request'
        if('result' in response):
            id = response['result']['id']
            return id
        print('Attempt',attempt,'failed.')
    print('Login failed!')

command_flows = {'connect': login_flow}

def main():

    player_id = None

    command_list =[key for key in command_args]


    while True:
        if not player_id:
            player_id = login_flow()
        print('\nCommand list')

        for i in range(0, len(command_list)):
            print(i,' - ', command_list[i])

        print('\n(',player_id,')Seclect command: ',end='')
        user_input = input()
        cmd_id = int(user_input)
        cmd = command_list[cmd_id]
        args = get_command_arguments(cmd)

        if cmd in command_flows:
            print(command_flows[cmd]())
        else:
            print(send_request(cmd,args,player_id))


if __name__ == "__main__":
    main()