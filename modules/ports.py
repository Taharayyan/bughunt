from core.executor import run

def scan():
    run("nmap -T4 -sV -iL results/alive.txt -oN results/nmap.txt")
