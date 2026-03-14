import subprocess
from concurrent.futures import ThreadPoolExecutor

def run(command: str):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")

def parallel(commands, workers: int = 4):
    with ThreadPoolExecutor(max_workers=workers) as executor:
        executor.map(run, commands)
