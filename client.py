import requests, json

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}

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


def merge_wizard(player_id, destination):
    '''

    '''
    args = {'new_conditions':{'merge': destination, 'state': 'ready'}}
    print_responce(send_request('wizard_conditions',args,player_id))

    return None

def print_responce(responce):

    def output_data(data,recursion_depth):

        if type(data) == type({}):
            print("+",end='')
            for block in data:
                print("\t"*recursion_depth,block)
                output_data(data[block],recursion_depth+1)
        elif type(data) == type([]):
            for block in data:
                output_data(block,recursion_depth+1)
        else:
            print("\t"*recursion_depth,data)



    if 'result' in responce:
        output_data(responce['result'],0)
        return None
        if type(responce['result']) not in (type(dict),type(list)):
            print(responce['result'])
            return None
        for block in responce['result']:
            print(block,"\n\t", responce['result'][block])
    else:
        print("Responce has failed\n",responce)