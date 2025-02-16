# sudo cp afl-clang-fast++ /usr/local/bin/

# Works:!
# cd /usr/local/bin/
# sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-clang-fast .
# sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-clang-fast++ .
# sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-showmap .

CC=afl-clang-fast CXX=afl-clang-fast++ ./build.sh --disable-shared

# afl-showmap -o /dev/null -- ./ugrep --help
# AFL_DEBUG=1; afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds

afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds

# https://github.com/SBULeeLab/LinguaFranca-FSE19/tree/master/data/production-regexes
# https://github.com/TheRenegadeCoder/sample-programs/tree/main/archive
