#!/bin/bash

CURRENT_DIR=$(pwd)

DIR1=funny_dir
DIR2=funny_dir_2

mkdir $DIR1
cd $DIR1
mkdir $DIR2
cd $DIR2

pwd

cd $CURRENT_DIR

rm -d $DIR1/$DIR2
rm -d $DIR1

cd /dev
pwd