import sys, requests, json

url = "http://localhost:4000/jsonrpc"
headers = {'content-type': 'application/json'}

def main():

    inp = '{"jsonrpc": "2.0", "params": {"login": "asd", "password": "123"}, "method": "connect", "id": 0}'
    inp = sys.stdin.readline()
    #print('input: ',inp)
    #inp = json.loads(inp)

    response = requests.post(url,
                             data=json.dumps(inp),
                             headers=headers).json()
    print(response)
    return None

if __name__ == "__main__":
    main()
