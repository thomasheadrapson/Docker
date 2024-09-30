import os
from typing import Dict
import requests

# adresse de l'API
address = 'localhost'

# port de l'API
port = 8001

# arguments
arguments : Dict[str,str] = dict()
        
# route
route = "status"

# expected status code
expected_status_code = 200


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
print(output.format(status_code = status_code, expected_status_code = expected_status_code, test_status = test_status, route = route, arguments = arguments))

# impression dans un fichier
if os.environ.get('LOG') == 1:
    with open('api_test.log', 'a') as file:
        file.write(output)