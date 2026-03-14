from core.executor import parallel

def run(target: str):

    commands = [
        f"subfinder -d {target} -silent -o results/subfinder.txt",
        f"assetfinder --subs-only {target} > results/assetfinder.txt"
    ]

    parallel(commands)

    merge = "cat results/subfinder.txt results/assetfinder.txt | sort -u > results/subdomains.txt"

    parallel([merge])
