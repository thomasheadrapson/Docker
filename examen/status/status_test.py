import os
from typing import Dict
import requests

# adresse de l'API
address = '172.18.0.2'

# port de l'API
port = 8000

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
    Status test
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
