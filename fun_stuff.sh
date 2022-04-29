#!/bin/sh
N=1000

for t in `seq 1 $N`
do
    echo ""
    echo "===================="
    echo "Test #$t results:"
    echo "===================="
    echo ""
    python3 knapsack_input.py test_input.txt 20
    echo "Exact Knapsack:"
    python3 max_knapsack.py < test_input.txt
    echo ""
    echo "Approximate Knapsack:"
    python3 knapsack_approximator.py < test_input.txt
    echo ""
    echo "Fractional Knapsack:"
    python3 cs412_lab7_b.py < test_input.txt
done > all_tests_output_all_knapsacks.txt