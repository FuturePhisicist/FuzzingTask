# 5 * 60 * 60 = 18000
# 5 * 60 * 60 + 60 = 18060, so that it terminates after the slaves

# export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/example.py`
# export AFL_PYTHON_MODULE=example

# export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/regex_mutator_1.py`
# export AFL_PYTHON_MODULE=regex_mutator_1

cd ~/msu/fuzzing_test/FuzzingTask

export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/regex_mutator_my.py`
export AFL_PYTHON_MODULE=regex_mutator_my

export AFL_CUSTOM_MUTATOR_ONLY=1 # if needed

afl-fuzz -i regexes_examples -o out_mutated_fuzz2 -M fuzzer01 -V 18060 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

afl-fuzz -i regexes_examples -o out_mutated_fuzz2 -S fuzzer02 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

afl-fuzz -i regexes_examples -o out_mutated_fuzz2 -S fuzzer03 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

afl-fuzz -i regexes_examples -o out_mutated_fuzz2 -S fuzzer04 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts