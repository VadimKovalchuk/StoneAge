import requests
import json, sys

player = None

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}
command_args = {'connect':['login', 'password'],
                'status':[],
                'wizard_conditions':['new_conditions_dict']}



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

    args = {"login": sys.argv[1], "password": sys.argv[2]}
    response = send_request('connect',args,0)
    assert response['id'] != str(0), 'Invalid ID is rescieved for connect request'
    if('result' in response):
        id = response['result']['id']
        return id

def update_wizard(player_id):
    '''

    '''
    args = {'new_conditions':{'merge': sys.argv[3], 'state': 'ready'}}
    print(send_request('wizard_conditions',args,player_id))

command_flows = {'connect': login_flow,
                 'wizard_conditions':update_wizard}

def main():
    command_list =[key for key in command_args]
    print(sys.argv)
    player_id = login_flow()
    print('AI '+ str(player_id) + '(' + sys.argv[1] + '/'+ sys.argv[2] +') is created. merging it to wizard '+ sys.argv[3])
    update_wizard(player_id)
    send_request('status',[],player_id)
    print(send_request('status',[],player_id))
    '''
    while True:
        print('\nCommand list')

        for i in range(0, len(command_list)):
            print(i,' - ', command_list[i])

        print('\n(',player_id,')Seclect command: ',end='')
        user_input = input()
        cmd_id = int(user_input)
        cmd = command_list[cmd_id]
        args = get_command_arguments(cmd)

        if cmd in command_flows:
            print(command_flows[cmd](player_id))
        else:
            print(send_request(cmd,args,player_id))
    '''

if __name__ == "__main__":
    main()