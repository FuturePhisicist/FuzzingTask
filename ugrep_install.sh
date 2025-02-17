# sudo cp afl-clang-fast++ /usr/local/bin/

# Works:!
# cd /usr/local/bin/
# sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-clang-fast .
# sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-clang-fast++ .
# sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-showmap .

CC=afl-clang-fast CXX=afl-clang-fast++ ./build.sh --disable-shared

# afl-showmap -o /dev/null -- ./ugrep --help
# AFL_DEBUG=1; afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds

sudo bash -c 'echo core >/proc/sys/kernel/core_pattern'
cd /sys/devices/system/cpu
sudo bash -c 'echo performance | tee cpu*/cpufreq/scaling_governor'
cd ~/msu/fuzzing_test/FuzzingTask

afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds

# https://github.com/SBULeeLab/LinguaFranca-FSE19/tree/master/data/production-regexes
# https://github.com/TheRenegadeCoder/sample-programs/tree/main/archive

# get uniq-regexes-8.json and archive respectively
