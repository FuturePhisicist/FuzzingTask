# afl-fuzz -i in_corpus -o out_fuzz -M fuzzer01 \
#   -- ./ugrep --color=never -e "test" @@

# afl-fuzz -i in_corpus -o out_fuzz -S fuzzer02 \
#   -- ./ugrep --color=never -e "test" @@

# 5 * 60 * 60 = 18000
# 5 * 60 * 60 + 60 = 18060, so that it terminates after the slaves

afl-fuzz -i regexes_examples -o out_fuzz -M fuzzer01 -V 18060 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

afl-fuzz -i regexes_examples -o out_fuzz -S fuzzer02 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

afl-fuzz -i regexes_examples -o out_fuzz -S fuzzer03 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts

afl-fuzz -i regexes_examples -o out_fuzz -S fuzzer04 -V 18000 -- ../ugrep/bin/ug -nr --color=never -e @@ input_texts