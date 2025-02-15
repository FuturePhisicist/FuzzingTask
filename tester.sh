#!/bin/sh

/home/fph/msu/fuzzing_test/AFL/afl-fuzz -i testcase_dir -o findings_dir -- ./test
