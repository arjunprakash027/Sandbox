import threading
import random
from typing import List, Tuple
import time

def create_matrix(n: int) -> Tuple:
    
    matrix1 = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
    matrix2 = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
    result_matrix = [[0] * n for _ in range(n)]

    return (matrix1, matrix2, result_matrix)

def matrix_multiply(A: List, B: List, result: List, row: int) -> None:
    
    n = len(A[0])
    m = len(A)

    print(f"Thread {row} starting...")  # Shows parallel execution

    for j in range(n):
        for k in range(m):
            result[row][j] += A[row][k] * B[k][j]
    
    print(f"Thread {row} finished! Result[{row}][0] = {result[row][0]}")


if __name__ == "__main__":
    
    n = 1000
    A, B, result = create_matrix(n)

    threads = []
    start = time.time()

    for i in range(n):

        t = threading.Thread(target=matrix_multiply, args=(A, B, result, i))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    elapsed = time.time() - start
    print(f"\nAFTER threading - result[0][0]: {result[0][0]}")
    print(f"Time: {elapsed:.4f}s")