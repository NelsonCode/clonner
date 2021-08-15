#!/bin/bash +x
PWD=`pwd`
/usr/local/bin/virtualenv --python=python3 venv
echo $PWD
activate () {
    . $PWD/venv/bin/activate
}

activate

pip3 install -r requirements.txt

python3 main.py $1 $2