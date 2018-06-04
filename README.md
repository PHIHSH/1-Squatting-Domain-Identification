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

Try the demo:  argv[1]=squatting domain , argv[2]=your domain

```
>>> python3 squatting_detect.py xn--fcebook-8va.com facebook.com
The analyzed domain and tld name is:
Domain facebook
TLD com
xn--fcebook-8va.com is a homo of facebook.com

------------------------------------------------------------
>>> python3 squatting_detect.py fcaebook.com facebook.com
The analyzed domain and tld name is:
Domain facebook
TLD com
fcaebook.com is a typo of facebook.com

------------------------------------------------------------
>>> python3 squatting_detect.py facebook.com google.com
The analyzed domain and tld name is:
Domain google
TLD com
Do not find the match

------------------------------------------------------------
>>> python3 squatting_detect.py alice-bo.com alice.com

there is no existing csv from URLcrazy, we begin to generate it

The analyzed domain and tld name is:
Domain alice
TLD com
alice-bo.com is a combo of alice.com

```

## FAST API

We provide a fast API to auto scan 100+ popular brands. No need to specify the brand domain.
```
------------------------------------------------------------
>>> python3 squating_API_fast_screen.py google-com.org
[Detection] [google-com.org] -> [google.com] -> [combo]
------------------------------------------------------------
>>> python3 squating_API_fast_screen.py google.tk
[Detection] [google.tk] -> [google.com] -> [wrongTLD]
------------------------------------------------------------
>>>  python3 squating_API_fast_screen.py facecook.com
[Detection] [facecook.com] -> [facebook.com] -> [bits]
------------------------------------------------------------
>>> python3 squating_API_fast_screen.py facedook.com
[Detection] [facedook.com] -> [facebook.com] -> [homo]
----------------------------------------------------------

```


### Dataset OpenSource (Benchmark)




## Squatting Methodology

We extend urlcrazy and DNStwist for more efficient squatting detection, by adding a lot of stuff.

URLcrazy-0.5:  https://www.morningstarsecurity.com/research/urlcrazy

DNStwist: https://github.com/elceef/dnstwist

+ increase homograph candidates

+ add combosquatting

+ make name consistent


## Disclaim and Reference

This is a research prototype, use at your own risk.