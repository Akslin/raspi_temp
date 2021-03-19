#!/bin/bash
./get_temp.sh >> temp.log
./get_temp.sh > actual_temp.log

python3 temp.py
cp index.html /var/www/html
