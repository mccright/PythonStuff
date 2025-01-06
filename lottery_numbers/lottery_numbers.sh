#!/bin/bash
echo -n "Powerball: " && shuf -i 1-69 -n 5 |  awk -vORS=' ' '{ print $1 }' && echo -n '- ' && shuf -i 1-26 -n 1 && echo -n "Mega-Millions: " && shuf -i 1-70 -n 5 |  awk -vORS=' ' '{ print $1 }' && echo -n '- ' && shuf -i 1-25 -n 1

