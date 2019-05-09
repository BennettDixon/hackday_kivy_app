#!/usr/bin/env bash
# script for building and spawning a backend
HOST_PORT=5000
CONT_PORT=5000

docker build -t bennettdixon16/hackday_kivy_app -f Dockerfile.dev .
echo -e "\n\nforwarding port $CONT_PORT from the docker container to port $HOST_PORT on the host\n\n"
docker run -p "$HOST_PORT:$CONT_PORT" bennettdixon16/hackday_kivy_app
