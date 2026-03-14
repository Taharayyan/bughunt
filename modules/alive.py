from core.executor import run

def run_alive():
    run("httpx -l results/subdomains.txt -title -status-code -tech-detect -o results/alive.txt")
