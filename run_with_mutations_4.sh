# 5 * 60 * 60 = 18000
# 5 * 60 * 60 + 60 = 18060, so that it terminates after the slaves

cd ~/msu/fuzzing_test/FuzzingTask

export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/regex_mutator_my1.py`
export AFL_PYTHON_MODULE=regex_mutator_my1

# export AFL_CUSTOM_MUTATOR_ONLY=1 # if needed

afl-fuzz -i unique_regexes -o final/with_mutator -S fuzzer04 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts
