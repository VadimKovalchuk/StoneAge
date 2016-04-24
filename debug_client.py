import requests
import json

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}

def main():

    print("login: ",end='')
    login = input()
    print("pass: ",end='')
    password = input()
    payload = {
            "method": "connect",
            "params": {"login": login, "password": password},
            "jsonrpc": "2.0",
            "id": 0,
        }
    response = requests.post(url,
                             data=json.dumps(payload),
                             headers=headers).json()
    assert response['id'] != str(0), 'Invalid ID is rescieved for connect request'
    my_id = response['result']['id']
    print(my_id,response['result']['session_type'])

    while True:
        print("Input function: ",end='')
        func= input()
        print("Input argument: ",end='')
        value = input()

        payload = {
            "method": func,
            "params": [value],
            "jsonrpc": "2.0",
            "id": 1,
        }
        response = requests.post(
            url, data=json.dumps(payload), headers=headers).json()
        print('Result ',response)

if __name__ == "__main__":
    main()