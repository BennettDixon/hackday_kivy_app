#!/usr/bin/env bash
# script for building and spawning a backend
HOST_PORT=5000
CONT_PORT=5000

docker build -t bennettdixon16/hackday_kivy_app -f Dockerfile.dev .
docker run -p "$HOST_PORT":"$CONT_PORT" bennettdixon16/hackday_kivy_app
