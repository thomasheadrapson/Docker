# status

curl -X GET -i http://localhost:8000/status

# Authentification

curl -X 'GET' 'http://localhost:8000/permissions?username=alice&password=wonderland' -H 'accept: application/json'

curl -X 'GET' 'http://localhost:8000/permissions?username=bob&password=builder' -H 'accept: application/json'

curl -X 'GET' 'http://localhost:8000/permissions?username=clementine&password=mandarine' -H 'accept: application/json'

# Authorization

curl -X 'GET' 'http://localhost:8000/permissions?username=alice&password=wonderland' -H 'accept: application/json'