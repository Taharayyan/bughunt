from core.executor import run

def scan():
    run("nuclei -l results/alive.txt -severity medium,high,critical -o results/vulns.txt")
