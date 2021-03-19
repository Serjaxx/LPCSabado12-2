#!/bin/bash
echo "introduce un numero mayor a 5 y menor a 15"
read x

if [ $x -gt 15 ]
then
        echo "te pasaste del 15, adios"
else
	echo "bien hecho, aqui vamos!"
	while [ $x -ge 0 ]
		do
        		echo "$x..."
        		x=$(( $x - 1 ))
	done
		echo "ENCENDIDO"
fi
