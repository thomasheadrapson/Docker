import os
from typing import Dict
import requests
import math

def run_test(credentials: Dict[str,str], expected_status_code: int, route: str, port: int, sentence: str = "", expected_score: int = 0):
    
    # requête
    arguments = credentials.copy()
    arguments["sentence"] = sentence
    
    r = requests.get(
        url = f'http://{address}:{port}/{route}/',
        params = arguments
        )

    output = '''
    ============================
        Content test
    ============================

    request done at "/{route}/"
    {credentials}
    for sentence
    "{sentence}"

    expected sentiment sign = {expected_score}
    actual sentiment score = {score_result}

    expected result = {expected_status_code}
    actual result = {status_code}
    
    ==>  {test_status}

    '''


    # statut de la requête
    status_code = r.status_code
    score_result = r.json()["score"]

    # affichage des résultats
    if math.copysign(1,score_result) == expected_score and status_code == expected_status_code:
        test_status = 'SUCCESS'
    else:
        test_status = 'FAILURE'
        
    output_text = output.format(score_result = score_result, status_code = status_code, expected_status_code = expected_status_code, expected_score = expected_score, test_status = test_status, route = route, credentials = credentials, sentence = sentence)

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
models = ["v1","v2"]


# arguments_list & expected_status_codes

credentials = {"username":"alice","password":"wonderland"}

sentence_list = [
    "life is beautiful",
    "that sucks",
    ]
scores_list = [1, -1]


for model in models:
    route = f"{model}/sentiment"
    for sentence, score in zip(sentence_list, scores_list):
        run_test(credentials, 200, route, port, sentence, score)
