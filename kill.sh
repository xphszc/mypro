# !/bin/bash

# kill myflask
kill $(pidof python myflask.py)

# echo message
echo 'myflask has killed'