# write a function to load environment variables from a .env file

import os

def load_env_variables(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The .env file at {path} does not exist.")
    
    with open(path, 'r') as env_file:
        for line in env_file:
            line = line.strip()
            if line and not line.startswith('#'):
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

# write a timing function to measure the execution time of a function

import time

def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time:.2f} seconds to execute.")
        return result
    return wrapper