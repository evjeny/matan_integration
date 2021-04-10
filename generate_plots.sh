#!/bin/bash

for n in "100" "1000"
do
    for choicer in "left" "right" "mid" "random"
    do
        conda run -n integrator python integrator.py -n $n -e $choicer --save_to "plots/n$n\_$choicer.png"
    done
done
