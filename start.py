import root,json_handle,db

def main():
    core = root.Core()
    gate = json_handle.Gate()
    database = db.Database()

    infra = {'core':core,'gate':gate,'database':database}
    for module in infra:
        infra[module].build_connections(infra)



    gate.start()

if __name__ == '__main__':
    main()