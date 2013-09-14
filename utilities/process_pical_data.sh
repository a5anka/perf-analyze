#! /bin/bash
# This script is used to generate arff files from pical data on ppc

#../data_viewer/PerfDataViewer.py ppical-good ../data/ppc/ppical-good_2_100000000.txt

PYTHON=python
SCRIPT="../data_viewer/PerfDataViewer.py"
data=(100000000 500000000 1000000000)
power7reducedevents="r2,r3c046,r2c048,r2f080,r26080,r30881,r26182,r26880,rd0a2,rd0a0"
PROGRAM=(ppical-good ppical-bad_fs)

for i in 1 2 4 8 16
do
    echo "------------------------------------------------"
    echo "No of threads ${i}"
    for d in ${data[@]}; do
        echo $d
        for program in ${PROGRAM[@]}; do
            echo $program 
            $PYTHON $SCRIPT ${program} "../data/ppc/${program}_${i}_${d}.txt" "../output/ppc/${program}_${i}_${d}.arff"
            echo
        done
    done
    echo
done

