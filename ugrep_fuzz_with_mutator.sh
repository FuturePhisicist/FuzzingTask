# 5 * 60 * 60 = 18000
# 5 * 60 * 60 + 60 = 18060, so that it terminates after the slaves

# export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/example.py`
# export AFL_PYTHON_MODULE=example

# export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/regex_mutator_1.py`
# export AFL_PYTHON_MODULE=regex_mutator_1

export PYTHONPATH=`dirname /home/fph/msu/fuzzing_test/FuzzingTask/mutator/regex_mutator_my.py`
export AFL_PYTHON_MODULE=regex_mutator_my

AFL_CUSTOM_MUTATOR_ONLY=1 afl-fuzz -i regexes_examples -o out_mutated_fuzz1 -M fuzzer01 -V 18060 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

AFL_CUSTOM_MUTATOR_ONLY=1 afl-fuzz -i regexes_examples -o out_mutated_fuzz1 -S fuzzer02 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

AFL_CUSTOM_MUTATOR_ONLY=1 afl-fuzz -i regexes_examples -o out_mutated_fuzz1 -S fuzzer03 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

AFL_CUSTOM_MUTATOR_ONLY=1 afl-fuzz -i regexes_examples -o out_mutated_fuzz1 -S fuzzer04 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts