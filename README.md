# Squatting Domain Identification
```

   _____                   _   _____  _     _     _
  / ____|                 | | |  __ \| |   (_)   | |
 | (___   __ _ _   _  __ _| |_| |__) | |__  _ ___| |__
  \___ \ / _` | | | |/ _` | __|  ___/| '_ \| / __| '_ \
  ____) | (_| | |_| | (_| | |_| |    | | | | \__ \ | | |
 |_____/ \__, |\__,_|\__,_|\__|_|    |_| |_|_|___/_| |_|
            | |
            |_|

```

Welcome to SquatPhish-squatting-identification!

Squatting-domain-dentification is part of SquatPhish project to identify squatting domains for popular brands.

It supports Five types of squatting identifications

- [x] Homograph Squatting
- [x] Typo Squatting
- [x] Bits Squatting
- [x] Combo Squatting
- [x] Wrong TLD


Examples could find here:

```
Original: facebook.com

Detected:

faceb00k.pw homo
facecook.us  bits
facrbook.com.br typo
facebook.online wrongTLD
facebook-fan.de combo

```

## Squatting Methodology

We extend urlcrazy and DNStwist for more efficient squatting detection, by adding a lot of stuff.

URLcrazy-0.5:  https://www.morningstarsecurity.com/research/urlcrazy

DNStwist: https://github.com/elceef/dnstwist

+ increase homograph candidates

+ add combosquatting

+ make name consistent

## Commands 

https://www.virustotal.com/en/url/fedfa28b317feda1399f28722016f421d2ccb9ae45bb7ac53b8aeeb628a2a595/analysis/

```bash
vt --url-report --url-scan /mnt/sdb1/mobilePhishing/DnsAnalysisEngine/dnsResovle/URL.txt

cat VT_report.txt| grep -n Positives/Total -A 5 -B 4
```