git clone https://github.com/AFLplusplus/AFLplusplus.git

cd /usr/local/bin/
sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-clang-fast .
sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-clang-fast++ .
sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-cmin .
sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-fuzz .
sudo ln -s /home/fph/msu/fuzzing_test/AFLplusplus/afl-showmap .

git clone https://github.com/Genivia/ugrep.git

CC=afl-clang-fast CXX=afl-clang-fast++ ./build.sh --disable-shared

# afl-showmap -o /dev/null -- ./ugrep --help
# AFL_DEBUG=1; afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds

sudo bash -c 'echo core >/proc/sys/kernel/core_pattern'
cd /sys/devices/system/cpu
sudo bash -c 'echo performance | tee cpu*/cpufreq/scaling_governor'
cd ~/msu/fuzzing_test/FuzzingTask

afl-showmap -o /dev/null -- ./bin/ugrep ugrepdsdfds
