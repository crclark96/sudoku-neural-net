#!/bin/bash

for file in {'msk_009.txt', 'subig20.txt', 'top100.txt', 'top2365.txt', 'top870.txt', 'top95.txt'} ; do
    
    python sudoku_v105.py $file

done