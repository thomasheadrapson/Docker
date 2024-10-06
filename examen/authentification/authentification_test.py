import os
from typing import Dict
import requests



def run_test(arguments: Dict[str,str], expected_status_code: int, route: str):
    
    # requête
    
    r = requests.get(
        url = f'http://{address}:{port}/{route}/',
        params = arguments
        )

    output = '''
    ============================
        Authentication test
    ============================

    request done at "/{route}/"
    {arguments}

    expected result = {expected_status_code}
    actual result = {status_code}

    ==>  {test_status}

    '''


    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == expected_status_code:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
        
    output_text = output.format(status_code = status_code, expected_status_code = expected_status_code, test_status = test_status, route = route, arguments = arguments)

    # impression dans un fichier
    if os.environ.get('LOG') == "1":
        print(output_text)
        with open('/home/logs/api_test.log', 'a') as file:
            file.write(output_text)
    
    return True

# adresse de l'API
address = '172.18.0.2'

# port de l'API
port = 8000

# route
route = "permissions"

# arguments_list & expected_status_codes

arguments_list = [{"username":"alice","password":"wonderland"},]
status_codes_list = [200,]

arguments_list.append({"username":"bob", "password":"builder"})
status_codes_list.append(200)

arguments_list.append({"username":"clementine", "password":"mandarine"})
status_codes_list.append(403)


for (args, code) in zip(arguments_list, status_codes_list):
    run_test(args, code, route)


