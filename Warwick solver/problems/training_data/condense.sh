#!/bin/bash

if [ -e ../training_data.txt ]
   then
      rm ../training_data.txt
fi

for file in ./*.txt
   do cat $file >> ../training_data.txt
done
