#!/bin/bash

if [[ $# != 1 || "$1" == "-h" ]]; then
	echo "Usage: `basename $0` <file>"
	exit 0
fi

var_all=$(awk '/ms/ {print $5}' $1 | tr "ms" "\0" | awk '{sum+=$1} END {print sum}')
var_player_1=$(cat $1 | grep ":B" | awk '/ms/ {print $5}' | tr "ms" "\0" | awk '{sum+=$1} END {print sum}')
var_player_2=$(cat $1 | grep ":W" | awk '/ms/ {print $5}' | tr "ms" "\0" | awk '{sum+=$1} END {print sum}')

duration=$(expr $var_all / 1000 / 60)


average_player_1=$(expr $var_player_1 / $(cat $1 | grep ":B" | wc -l))
average_player_2=$(expr $var_player_2 / $(cat $1 | grep ":W" | wc -l))

echo -n La partie a duré $duration minute
if [ $duration != 1 ]; then
	echo -n s
fi
printf ".\n\n"

echo Le joueur B a pris en moyenne $average_player_1 ms pour faire ses actions.
echo Le joueur W a pris en moyenne $average_player_2 ms pour faire ses actions.

if grep -q "(IA):W" "$1"; then
	printf "\nL'IA jouait les W."
elif grep -q "(IA):B" "$1"; then
	printf "\nL'IA jouait les B."
else
	printf "\nIl n'y avait pas d'IA dans la partie."
fi

echo
