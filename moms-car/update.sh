#!/bin/bash

rm -rf backup
mkdir backup
mv release/* backup
rm -rf release
mkdir release
cp -r dev/moms-car/* release

