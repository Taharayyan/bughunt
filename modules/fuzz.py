from core.executor import parallel

def run(target: str):

    commands = [
        f"ffuf -u https://{target}/FUZZ -w wordlists/common.txt -o results/ffuf.json",
        f"feroxbuster -u https://{target} -o results/ferox.txt"
    ]

    parallel(commands)
