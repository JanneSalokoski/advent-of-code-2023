import functools
import inspect
import time
import os

def timer(func):
    """Time the execution of a function"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()

        print(f"Function {func.__name__!r} executed in {(t2-t1):.4f}s")
        return result
    return wrapper

def get_input():
    """Read input for the days script from file and strip it"""
    file = os.path.join("./inputs/", inspect.stack()[3].filename.replace(".py", ".txt"))
    with open(file, "r") as f:
        return f.read().strip()

def get_sample():
    """Read sample imput instead of real input"""
    file = os.path.join("./inputs/", inspect.stack()[3].filename.replace(".py", "-sample.txt"))
    with open(file, "r") as f:
        return f.read().strip()

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

