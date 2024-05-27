#!/bin/bash

rm -rf instance
echo "delete old data"

python app.py &
echo "run app.py"

sleep 2
pkill -f app.py
echo "kill app.py"


./add.sh
echo "run add.sh"

flask run --host=0.0.0.0
echo "run flask website"