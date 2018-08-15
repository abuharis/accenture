#!/usr/bin/bash

if [ $# -ge 1 ]
then
	echo "Wrong Usage! "
	exit 1
fi


VAR=$[ $RANDOM % 10 ]

while true
do
	echo "Enter your number"
	read number
		if [ -z $number ]
		then
			echo "Error:Enter one Number"
			continue
		fi
	if [ $number -gt $VAR ]
	then
		echo "Too Big! :) "
	elif [ $number -lt $VAR ]
	then
		echo "Too Small"
	else
		echo "YOU WIN"
		exit 0
	fi
done
