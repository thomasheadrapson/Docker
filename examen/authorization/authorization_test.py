import os
from typing import Dict, Literal
import requests



def run_test(arguments: Dict[str,str], expected_status_code: int, route: str) -> Literal[True]:
    # requête
    r = requests.get(
        url = f'http://{address}:{port}/{route}/{route_base}/',
        params = arguments
        )

    output = '''
    ============================
        Authorisation test
    ============================

    request done at "/{route}/{route_base}/"
    {arguments}

    expected result = {expected_status_code}
    actual restult = {status_code}

    ==>  {test_status}

    '''


    # statut de la requête
    status_code = r.status_code

    # affichage des résultats
    if status_code == expected_status_code:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(status_code = status_code, expected_status_code = expected_status_code, test_status = test_status, route = route, route_base = route_base, arguments = arguments))

    # impression dans un fichier
    if os.environ.get('LOG') == 1:
        with open('api_test.log', 'a') as file:
            file.write(output)
    
    return True

# adresse de l'API
address = 'localhost'

# port de l'API
port = 8001

# route
route_base = "sentiment"
routes = ["v1","v2"]


# arguments_list & expected_status_codes

arguments_list = [{"username":"alice","password":"wonderland"},]
status_codes_list = [(200, 200),]
arguments_list.append({"username":"bob", "password":"builder"})
status_codes_list.append((200, 403),)


for args, codes in zip(arguments_list, status_codes_list):
    for route, code in zip(routes, codes):
        run_test(args, code, route)


