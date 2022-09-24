#!/usr/bin/env bash

case "$1" in
    build)
        python3 -m pip install --upgrade pip
        python3 -m pip install --no-cache-dir -r requirements.txt
    ;;
    start)
        nohup python3 -m uvicorn main:app --reload --host 0.0.0.0 --port 8080 > app.log 2>&1 &
        echo $! > app_pid.txt
    ;;

    stop)
        kill -9 `cat save_pid.txt`
        rm app_pid.txt
    ;;

    *)
      echo "Options are:"
      echo "install | Install dependencies and build image"
      echo "start | Start the application"
      echo "start | Stop the application"
    ;;
esac
