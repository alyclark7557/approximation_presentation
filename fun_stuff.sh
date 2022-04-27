#!/bin/sh
N=10

for t in `seq 3 $N`
do
    echo ""
    echo "Test with $t inputs:"
    echo ""
    python3 knapsack_input.py test_input.txt $t
    python3 max_knapsack.py < test_input.txt
done > all_tests_output.txt