import ray
import random
from typing import List, Tuple
import time

random.seed(69)

def create_matrix(n: int) -> Tuple:
    
    matrix1 = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
    matrix2 = [[random.randint(0, 100) for _ in range(n)] for _ in range(n)]
    result_matrix = [[0] * n for _ in range(n)]

    return (matrix1, matrix2, result_matrix)

@ray.remote
def matrix_multiply(A: List, B: List, row: int) -> List:
    
    n = len(A)
    result_row = [0] * n

    #print(f"Thread {row} starting...")  # Shows parallel execution

    for j in range(n):
        for k in range(n):
            result_row[j] += A[row][k] * B[k][j]
    
    return result_row
    #print(f"Thread {row} finished! Result[{row}][0] = {result[row][0]}")


if __name__ == "__main__":
    
    n = 500
    A, B, result = create_matrix(n)

    threads = []
    start = time.time()

    futures = [matrix_multiply.remote(A,B,i) for i in range(n)]

    result = ray.get(futures)
    
    elapsed = time.time() - start
    print(f"\nAFTER threading - result[0][0]: {result[0][0]}")
    print(f"Time: {elapsed:.4f}s")