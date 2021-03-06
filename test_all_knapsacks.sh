#!/bin/sh
N=43

for t in `seq 1 1`
do
    echo ""
    echo "============================"
    echo "Test with $N inputs 200 weight results:"
    echo "============================"
    echo ""
    echo "Exact Knapsack:"
    python3 exact_knapsack.py < final_test_for_weight_200_tests.txt
    echo ""
    echo "Approximate Knapsack:"
    python3 knapsack_approximator.py < final_test_for_weight_200_tests.txt
    echo ""
    echo "Fractional Knapsack:"
    python3 cs412_lab7_b.py < final_test_for_weight_200_tests_copy.txt
done > final_results_200_weight_all_knapsacks.txt
