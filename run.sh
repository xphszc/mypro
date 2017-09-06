# !/bin/bash

echo 'try start flask ----'

# delete log.txt
rm log.txt

# run myflask in back
# log in log.txt
nohup python myflask.py > log.txt 2>&1 &

# catlog log.txt info
cat log.txt

echo 'start flask OK !'