import time
from contextlib import contextmanager
from typing import Optional

@contextmanager
def timer(description: str = "Operation"):
    start = time.time()
    yield
    elapsed_time = time.time() - start
    print(f"{description} took: {elapsed_time:.2f} seconds")