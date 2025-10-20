import ray

ray.init()

@ray.remote
def sq(n: int) -> int:

    return n * n

future = [sq.remote(i) for i in range(5)]

results = ray.get(future)

print(results)