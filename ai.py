import sys, time, client

player = None

def login_flow():
    '''

    '''
    args = {"login": sys.argv[1], "password": sys.argv[2]}
    response = client.send_request('connect',args,0)
    assert response['id'] != str(0), 'Invalid ID is rescieved for connect request'
    if('result' in response):
        id = response['result']['id']
        return id

def update_wizard(player_id):
    '''

    '''
    args = {'new_conditions':{'merge': sys.argv[3], 'state': 'ready'}}
    print(client.send_request('wizard_conditions',args,player_id))

command_flows = {'connect': login_flow,
                 'wizard_conditions':update_wizard}

def main():

    #print(sys.argv)
    player_id = login_flow()
    print('AI '+ str(player_id) + '(' + sys.argv[1] + '/'+ sys.argv[2] +') is created. merging it to wizard '+ sys.argv[3])
    update_wizard(player_id)
    #send_request('status',[],player_id)
    #print(send_request('status',[],player_id))

    for i in range(0,10):
        print('AI '+ str(player_id) + '(' + sys.argv[1] + '/'+ sys.argv[2] +'):'+ str(client.send_request('status',[],player_id)))
        time.sleep(5)

if __name__ == "__main__":
    main()