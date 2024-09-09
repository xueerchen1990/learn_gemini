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