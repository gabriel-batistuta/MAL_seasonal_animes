import json

class Json:
    def writeJson(self, client_id):
        config = {'X-MAL-CLIENT-ID':client_id}

        with open('.client_ID.json', 'w') as file:
            json.dump(config, file, indent=4)
        return True

    def readJson(self):
        with open('.client_ID.json', 'r') as file:
            config = json.load(file)
        return config

if __name__ == '__main__':

    # id: https://myanimelist.net/apiconfig
    
    client_id = 'coloque seu ID do MAL aqui'

    Json().writeJson(client_id)