#!/bin/bash

TARGET=$1
DATE=$(date +%Y%m%d_%H%M)
OUT="recon_$TARGET_$DATE"

echo "[+] Starting recon for $TARGET"

mkdir -p $OUT
cd $OUT

echo "[+] Subdomain enumeration"

subfinder -d $TARGET -silent > sub1.txt
assetfinder --subs-only $TARGET > sub2.txt

cat sub1.txt sub2.txt | sort -u > subdomains.txt

echo "[+] Resolving live domains"

dnsx -l subdomains.txt -silent > resolved.txt

echo "[+] Detecting live web services"

httpx -l resolved.txt -silent -status-code -title -tech-detect > alive_full.txt

cat alive_full.txt | awk '{print $1}' | sed 's|https://||;s|http://||' > alive.txt

echo "[+] Port scanning"

naabu -l alive.txt -top-ports 1000 -silent > ports.txt

nmap -iL alive.txt -sV -T4 -Pn -oN nmap.txt

echo "[+] Collecting URLs"

gau $TARGET > gau.txt

echo "[+] Crawling endpoints"

katana -u https://$TARGET -depth 3 -silent > katana.txt

cat gau.txt katana.txt | sort -u > endpoints.txt

echo "[+] Directory fuzzing"

ffuf -w /usr/share/seclists/Discovery/Web-Content/common.txt \
-u https://$TARGET/FUZZ \
-t 40 \
-o ffuf.json

echo "[+] Running vulnerability scan"

nuclei -l alive.txt -severity medium,high,critical -o vulns.txt

echo "[+] Recon finished"

echo "Results saved in:"
pwd
