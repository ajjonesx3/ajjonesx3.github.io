#!/bin/bash

python3 dev/moms-car/scripts/main.py
rm -rf backup
mkdir backup
mv release/* backup
rm -rf release
mkdir release
cp -r dev/moms-car/* release

