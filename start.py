import root
import json_handle

def main():
    core = root.Core()
    gate = json_handle.Gate()

    infra = [core,gate]
    for module in infra:
        module.build_connections()



    gate.start()

if __name__ == '__main__':
    main()