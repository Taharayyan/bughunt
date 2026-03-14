from core.executor import run

def crawl():
    run("katana -list results/alive.txt -depth 3 -o results/crawled.txt")
