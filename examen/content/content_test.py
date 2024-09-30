import os
from typing import Dict, Literal
import requests
import math



def run_test(args: Dict[str,str], expected_score: int, route: str, sentence: str) -> Literal[True]:
    
    # params
    
    arguments = credentials.copy()
    arguments["sentence"] = sentence
    
    # requête
    
    r = requests.get(
        url = f'http://{address}:{port}/{route}/{route_base}/',
        params = arguments
        )

    output = '''
    ============================
        Content test
    ============================

    request done at "/{route}/{route_base}/"
    {credentials}
    for sentence
    "{sentence}"

    expected sentiment sign = {expected_score}
    actual sentiment score = {score_result}

    ==>  {test_status}

    '''

    print(r.json())
    # statut de la requête
    score_result = r.json()["score"]

    # affichage des résultats
    if math.copysign(1,score_result) == expected_score:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
    print(output.format(score_result = score_result, expected_score = expected_score, test_status = test_status, route = route, route_base = route_base, credentials = credentials, sentence = sentence))

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

credentials = {"username":"alice","password":"wonderland"}

sentence_list = [
    "life is beautiful",
    "that sucks",
    ]
scores_list = [1, -1]


for route in routes:
    for sentence, score in zip(sentence_list, scores_list):
        run_test(credentials, score, route, sentence)
