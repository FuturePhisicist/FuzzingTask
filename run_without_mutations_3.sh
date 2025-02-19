# 5 * 60 * 60 = 18000
# 5 * 60 * 60 + 60 = 18060, so that it terminates after the slaves

cd ~/msu/fuzzing_test/FuzzingTask

unset PYTHONPATH
unset AFL_PYTHON_MODULE
unset AFL_CUSTOM_MUTATOR_ONLY

afl-fuzz -i unique_regexes -o final/without_mutator -S fuzzer03 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts
