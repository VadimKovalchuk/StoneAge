import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

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