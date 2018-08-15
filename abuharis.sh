#!/usr/bin/bash

#Exit Codes



case "$1" in
	start)
		echo "starting programme"

	stop )
		echo "stoping programmme"
	restart )
		echo "restarting programme"
	*)
		echo "nothing is happening"
esac


if [ $# -lt 1 ]
then
	echo "Error:Atleast one argument required"
	exit 1
else

echo "Hello world"
echo "Error: we have some problem" >&2

#Variable assign

FIRST=ABUHARIS
SURNAME=SALIH


echo "Hai $FIRST, Today is $(date)"

#Arithmetic

echo $[ ( 1 + 2 ) *3 ]

echo $[ (100 + 200) % (3 + 8) ]
#set -x
#COUNT=1
#for FILE in $(ls  $HOME) 
#do 
	echo $COUNT $FILE
	COUNT=$[ COUNT + 1 ]
#set +x
#done

#Arguments

for ARG in "$*"
do
	echo "Argumets: $ARG"
done


for ARG in $@
do
	echo "Argumets: $ARG"
done


echo "There are $# arguments"


for ARG in "$*"
do
	echo "Argumets: $ARG"
done



exit 0

fi


