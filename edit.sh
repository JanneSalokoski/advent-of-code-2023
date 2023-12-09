#!/bin/sh
set -eu

nvim day-$1.py inputs/day-$1.txt inputs/day-$1-sample.txt
