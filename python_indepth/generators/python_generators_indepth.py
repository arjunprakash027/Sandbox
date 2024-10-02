import time
from collections import deque
from typing import Generator, Deque, Tuple

# Generator functions simulating async behavior
def infi(id: int) -> Generator:
    num = 0
    while True:
        print(f"infi {id}: {num}")
        num += 1
        yield id  # Yield control with a delay equivalent to the id

def print_name(prefix: str) -> Generator:
    print(f"Searching for prefix: {prefix}")
    while True:
        name = yield  # Yield here to receive a name
        if name and prefix in name:
            print(f"Found: {name}")
        yield 1  # Simulate work with a 1-second delay

def passinput() -> Generator:
    print("passinput coroutine started.")
    while True:
        val = yield  # Yield here to receive a value
        if val is not None:
            print(f"Received: {val}")
        yield 1  # Simulate work with a 1-second delay

# Scheduler to manage coroutines
class TaskScheduler:
    def __init__(self):
        self.tasks: Deque[Tuple[float, Generator]] = deque()

    def add_task(self, task: Generator):
        # Add task to the queue with the current time
        self.tasks.append((time.time(), task))

    def run(self):
        while self.tasks:
            current_time = time.time()
            wake_up_time, task = self.tasks.popleft()
            
            if current_time >= wake_up_time:
                try:
                    # Run the task until the next yield
                    delay = next(task)
                    if delay is None:
                        delay = 0
                    # Re-add the task with its next wake-up time
                    self.tasks.append((current_time + delay, task))
                except StopIteration:
                    print("Task completed")
            else:
                # Re-enqueue the task and sleep briefly
                self.tasks.append((wake_up_time, task))
                time.sleep(0.01)

if __name__ == '__main__':
    # Initialize the scheduler
    scheduler = TaskScheduler()

    # Create and add tasks
    scheduler.add_task(infi(1))
    scheduler.add_task(infi(2))
    scheduler.add_task(infi(3))
    scheduler.add_task(print_name("Dear"))
    scheduler.add_task(passinput())

    # Run the scheduler
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Scheduler stopped.")
