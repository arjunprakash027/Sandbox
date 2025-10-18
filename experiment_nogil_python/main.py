import sys

def main():
    print("Hello from experiment-nogil-python!")
    print(sys._is_gil_enabled())


if __name__ == "__main__":
    main()
