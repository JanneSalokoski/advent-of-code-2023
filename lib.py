import functools
import inspect
import time
import os

import logging
logger = logging.getLogger(__name__)

def timer(func):
    """Time the execution of a function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.perf_counter()
        result = func(*args, **kwargs)
        t2 = time.perf_counter()

        logger.debug(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result
    return wrapper

@functools.cache
def read_file(file):
    with open(file, "r") as f:
        return f.read().strip()

def get_input():
    """Read input for the days script from file and strip it"""
    file = os.path.join("./inputs/", inspect.stack()[3].filename.split("/")[-1].replace(".py", ".txt"))
    logger.debug(f"Reading input from: {file}")
    return read_file(file)

def get_sample():
    """Read sample input instead of real input"""
    file = os.path.join("./inputs/", inspect.stack()[3].filename.split("/")[-1].replace(".py", "-sample.txt"))
    logger.debug(f"Reading input from: {file}")
    return read_file(file)

def aoc_input(func):
    """Call `func` with aoc-input as an argument"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        text = get_input()
        return func(*args, text=text, **kwargs)

    return wrapper

def aoc_sample(func):
    """Call `func` with aoc-sample as an argument"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        text = get_sample()
        return func(*args, text=text, **kwargs)

    return wrapper

@aoc_sample
def test_sample(text=""):
    logger.debug(f"text: {text}") 

def test():
    test_sample()

if __name__ == "__main__":
    test()
