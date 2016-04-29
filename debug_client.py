import requests
import json

player = None
url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}
command_list = {'connect':['login', 'password'],
                'status':['player_id']}


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
    if(name in command_list):
        params = {}
        for argument in command_list[name]:
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
        if args:
            response = send_request('connect',args,0)
        assert response['id'] != str(0), 'Invalid ID is rescieved for connect request'
        if('result' in response):
            id = response['result']['id']
            return id
        print('Attempt',attempt,'failed.')
    print('Login failed!')


def main():

    command_flows = {'connect': login_flow()}

    player_id = login_flow()

    print(player_id)

    while True:
        if not player_id:
            print('YOU ARE NOT AUTHORIZED!!! Enter "connect" to login.')
        print('\nCommand list')
        for command in command_list:
            print(command)
        print('\n(',player_id,')Seclect command: ',end='')
        cmd = input()
        args = get_command_arguments(cmd)
        if args:
            print(send_request(cmd,args,player_id))


if __name__ == "__main__":
    main()