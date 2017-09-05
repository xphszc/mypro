# !/bin/bash

echo 'start flask ----'

# run myflask in back
# log in log.txt
nohup python myflask.py > log.txt 2>&1 &

echo 'start flask OK !'