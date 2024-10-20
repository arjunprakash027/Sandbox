# Compiler and flags
CXX = g++
CXXFLAGS = -O3 -Wall -shared -std=c++11 -fPIC
PYBIND_FLAGS = `python3 -m pybind11 --includes`
PYTHON_CONFIG = `python3-config --extension-suffix`

# Source files
SRCS = array_utilities.cpp py_bind.cpp 

# Output file name
TARGET = example$(PYTHON_CONFIG)

# Rule to create the shared object
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) $(PYBIND_FLAGS) $(SRCS) -o $(TARGET)

# Clean rule to remove generated files
clean:
	rm -f $(TARGET)
