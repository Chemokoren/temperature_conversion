#!/bin/sh

ssh root@34.238.153.190 <<EOF
  cd temperature_conversion
  git pull
  source /opt/envs/temperature_conversion/bin/activate
  pip install -r requirements.txt
  ./manage.py migrate
  sudo supervisorctl restart djtrump
  exit
EOF