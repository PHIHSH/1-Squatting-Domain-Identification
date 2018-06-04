# Squatting Domain Identification
```

   _____                   _   _____  _     _     _
  / ____|                 | | |  __ \| |   (_)   | |
 | (___   __ _ _   _  __ _| |_| |__) | |__  _ ___| |__
  \___ \ / _` | | | |/ _` | __|  ___/| '_ \| / __| '_ \
  ____) | (_| | |_| | (_| | |_| |    | | | | \__ \ | | | - Identification
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

## Set up
```
bash install.sh
```

## APIs


Try the demo:  argv[1]=squatting domain , argv[2]=original domain

```
>>> python3 squatting_detect.py xn--fcebook-8va.com facebook.com                                                                                                                ketian@ketian
The analyzed domain and tld name is:
Domain facebook
TLD com
xn--fcebook-8va.com is a homo of facebook.com

------------------------------------------------------------
>>> python3 squatting_detect.py fcaebook.com facebook.com                                                                                                                       ketian@ketian
The analyzed domain and tld name is:
Domain facebook
TLD com
fcaebook.com is a typo of facebook.com

```


### FAST API


### Identification for your own brand


### Run the Demo (Benchmark)



## Squatting Methodology

We extend urlcrazy and DNStwist for more efficient squatting detection, by adding a lot of stuff.

URLcrazy-0.5:  https://www.morningstarsecurity.com/research/urlcrazy

DNStwist: https://github.com/elceef/dnstwist

+ increase homograph candidates

+ add combosquatting

+ make name consistent


## Disclaim and Reference

This is a research prototype, use at your own risk.