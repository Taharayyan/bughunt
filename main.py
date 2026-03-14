import os

from modules import subdomains
from modules import alive
from modules import ports
from modules import urls
from modules import crawler
from modules import fuzz
from modules import vulnscan

from core.logger import log
from core.reporter import generate


def main():

    target = input("Target domain: ").strip()

    os.makedirs("results", exist_ok=True)

    log("Starting subdomain enumeration")
    subdomains.run(target)

    log("Detecting live hosts")
    alive.run_alive()

    log("Running port scan")
    ports.scan()

    log("Collecting URLs")
    urls.collect(target)

    log("Crawling endpoints")
    crawler.crawl()

    log("Running directory fuzzing")
    fuzz.run(target)

    log("Running vulnerability scan")
    vulnscan.scan()

    generate()


if __name__ == "__main__":
    main()
