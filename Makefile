CXX=/home/fph/msu/fuzzing_test/AFL/afl-g++
CXXFLAGS=-O2 -g
TARGET=test
SRC=test.cpp

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRC)

clean:
	rm $(TARGET)
