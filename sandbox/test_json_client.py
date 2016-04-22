import requests
import json


def main():
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    # Example echo method
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    print(response["result"] == "echome!")
    print(response["jsonrpc"] == "2.0")
    print(response["id"] == 0)


    # Example echo method JSON-RPC 1.0
    payload = {
        "method": "echo",
        "params": ["echome!"],
        "id": 0,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    print(response["result"] == "echome!")
    #print(response["error"])
    print(response["id"] == 0)
    print("jsonrpc" not in response)


    # Example add method
    payload = {
        "method": "add",
        "params": [1, 2],
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    print(response["result"] == 3)
    print(response["jsonrpc"] == "2.0")
    print(response["id"] == 1)


    # Example foobar method
    payload = {
        "method": "foobar",
        "params": {"foo": "json", "bar": "-rpc"},
        "jsonrpc": "2.0",
        "id": 3,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response)
    #print(response["result"] == "json-rpc")
    print(response["jsonrpc"] == "2.0")
    print(response["id"] == 3)


    # Example exception
    payload = {
        "method": "add",
        "params": [0],
        "jsonrpc": "2.0",
        "id": 4,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response)
    print(response["error"]["message"] == "Invalid params")
    print(response["error"]["code"] == -32602)
    print(response["jsonrpc"] == "2.0")
    print(response["id"] == 4)


    payload = {
        "method": "pussy",
        "params": ['fagot','qwe'],
        "jsonrpc": "2.0",
        "id": 5,
    }
    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()
    print(response['result'])


if __name__ == "__main__":
    main()