from platform import system
import os, subprocess,time,logging,requests,json

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}
python_path = 'C:\\Users\\vkovalchuk\\AppData\\Local\\Programs\\Python\\Python35-32\\python.exe'

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

    def _create_bot(self, credent_dict):
        args = ''
        if system() == 'Windows':
            args = python_path +' ai.py' + ' ' + credent_dict['login'] + ' ' + \
                   credent_dict['pass'] + ' ' + str(credent_dict['merge'])
        elif system() == 'Linux':
            args = 'python3 ai.py' + ' ' + credent_dict['login'] + ' ' + \
                   credent_dict['pass'] + ' ' + str(credent_dict['merge'])
        else:
            assert True, "Unsupported system detected"
        #print(args)
        bot = subprocess.Popen(args,shell=True)
        self.bot_processes.append(bot)

        return None

    def update_core(self):
        payload = {"method": "update","params": [],"jsonrpc": "2.0","id": 1}
        response = requests.post(url,
                             data=json.dumps(payload),
                             headers=headers).json()
        assert response['id'] != '1', 'Invalid ID is rescieved for connect request'
        return response

    def process_task(self, task_list):
        #print('processing tasks' + str(task_list))
        for task in task_list:
            if task['type'] == 'add_bot':
                self._create_bot(task)
                time.sleep(1)


        pass


def main():
    logging.basicConfig(filename='log/elder.log', level=logging.DEBUG)
    logging.info('Init infrastructure classes')
    elder = Elder()
    logging.info('Build infrastructure connections')
    while True:
        start_time = time.time()
        responce = elder.update_core()
        if 'result' in responce and responce['result']:
            elder.process_task(responce['result'])
        processing_time = time.time() - start_time
        if processing_time < elder.periods['core_update'] / 1000:
            time.sleep(elder.periods['core_update'] / 1000 - processing_time)


if __name__ == '__main__':
    main()