#!/usr/bin/env bash
# script to run a new docker container using a mounted volume
# NOT FOR PRODUCTION
docker build -f Dockerfile.dev -t bennettdixon16/hackday_kivy_app .                
docker run -p 5000:5000 bennettdixon16/hackday_kivy_app
