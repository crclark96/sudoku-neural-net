#!/bin/bash

if [ -e ../test_data.txt ]
   then
      rm ../test_data.txt
fi

for file in ./*.txt
   do cat $file >> ../test_data.txt
done
