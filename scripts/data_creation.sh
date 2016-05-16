#!/bin/bash

kw=(mort mourir suicide)

for (( i=0; i < ${#kw[@]}; i++ )); 
do

python main.py ${kw[i]} ${kw[i]}
done

exit 0