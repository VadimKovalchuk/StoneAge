import requests, json, client

player = None

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}
command_args = {'login':['login', 'password'],
                'status':[],
                'merge_wizard':['destination'],
                'player_data':['player_id']}


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
    for attempt in range(1,4):
        args = get_command_arguments('login')
        response = client.send_request('connect',args,0)
        assert response['id'] != str(0), 'Invalid ID is rescieved for connect request'
        if('result' in response):
            id = response['result']['id']
            return id
        print('Attempt',attempt,'failed.')
    print('Login failed!')

def update_wizard(player_id):
    '''

    '''
    args = {'new_conditions':{'merge': '1000', 'state': 'ready'}}
    print(client.send_request('wizard_conditions',args,player_id))

def main():

    player_id = login_flow()

    command_list =[key for key in command_args]


    while True:
        print('\nCommand list')

        for i in range(0, len(command_list)):
            print(i,' - ', command_list[i])

        print('\n(',player_id,')Seclect command: ',end='')
        user_input = input()
        cmd_id = int(user_input)
        cmd = command_list[cmd_id]
        args = get_command_arguments(cmd)

        if cmd == 'login':
            client.print_responce(login_flow())
        elif cmd == 'merge_wizard':
            client.merge_wizard(player_id,args['destination'])
        else:
            client.print_responce(client.send_request(cmd,args,player_id))


if __name__ == "__main__":
    main()