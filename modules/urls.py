from core.executor import run

def collect(target: str):
    run(f"gau {target} > results/gau_urls.txt")
