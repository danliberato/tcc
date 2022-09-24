#!/usr/bin/env bash

case "$1" in
    build)
#        docker build -t javi_api .
        python3 -m pip install --upgrade pip
        python3 -m pip install --no-cache-dir -r requirements.txt
    ;;
    start)
        python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8080
#        docker run javi_api
    ;;

    stop)
#        docker stop
#        docker rm api_$(echo $2)
        echo "Commando WIP"
    ;;

    *)
      echo "Options are:"
      echo "install | Install dependencies and build image"
      echo "start | Start the application"
      echo "start | Stop the application"
    ;;
esac