from platform import system
import os, subprocess,time,logging,requests,json

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}

class Elder:
    '''
    Server infrastructure controller.
    Current task list:
     - periodic Core update
     - in case if Core is crashed - restart it(optional)(not implemented)
     - create and maintain bots processes (not implemented)
     - periodic source code update from main branch (not implemented)
     - TBD
    '''

    def __init__(self):
        '''
        (None) -> None

        Initial class creation. Without connection to infrastructure.
        '''
        self.core_session = None
        self.bot_processes = []  # Running bot processes
        self.requests = []  # Requests that sent by Core
        self.periods = {'core_update': 1000,
                        'process_creation': 1000,
                        'git_update': 3600000}
        logging.debug('Elder is running')

        return None

    def update_core(self):
        payload = {"method": "update","params": [],"jsonrpc": "2.0","id": 1}
        response = requests.post(url,
                             data=json.dumps(payload),
                             headers=headers).json()
        assert response['id'] != '1', 'Invalid ID is rescieved for connect request'
        return response


def main():
    logging.basicConfig(filename='log/elder.log', level=logging.DEBUG)
    logging.info('Init infrastructure classes')
    elder = Elder()
    logging.info('Build infrastructure connections')
    while True:
        start_time = time.time()
        responce = elder.update_core()
        if responce['result']:
            print('processing tasks' + str(responce))
        processing_time = time.time() - start_time
        print('utilization: '+ str(processing_time * 1000 / elder.periods['core_update']))
        time.sleep(elder.periods['core_update'] / 1000 - processing_time)


if __name__ == '__main__':
    main()