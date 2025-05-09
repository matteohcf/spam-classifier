import os
from dotenv import load_dotenv

def load_env():
    for env_file in ['.env', '.env.local']:
        env_path = os.path.join(os.getcwd(), env_file)
        if os.path.exists(env_path):
            load_dotenv(env_path)
