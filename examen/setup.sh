docker image pull datascientest/fastapi:1.0.0

docker image build ./status -t status:latest

docker image build ./authentification -t authentification:latest

docker image build ./authorization -t authorization:latest

docker image build ./content -t content:latest

export LOG="1"

docker compose up