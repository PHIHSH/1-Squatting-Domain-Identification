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

# Squatting Domain Identification

Squatting-domain-dentification is part of SquatPhish project to identify squatting domains for popular brands.

It supports Five types of squatting identifications



## Squatting

We extend urlcrazy and DNStwist for more efficient squatting detection.

URLcrazy-0.5:  https://www.morningstarsecurity.com/research/urlcrazy

DNStwist: https://github.com/elceef/dnstwist

+ add combosquatting


## Commands 

https://www.virustotal.com/en/url/fedfa28b317feda1399f28722016f421d2ccb9ae45bb7ac53b8aeeb628a2a595/analysis/

```bash
vt --url-report --url-scan /mnt/sdb1/mobilePhishing/DnsAnalysisEngine/dnsResovle/URL.txt

cat VT_report.txt| grep -n Positives/Total -A 5 -B 4
```