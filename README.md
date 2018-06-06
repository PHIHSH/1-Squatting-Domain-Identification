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

Squatting-Domain-Identification is part of SquatPhish project to identify squatting domains for popular brands.

It supports Five types of squatting identifications

- [x] Homograph Squatting
- [x] Typo Squatting
- [x] Bits Squatting
- [x] Combo Squatting
- [x] Wrong TLD

```
Traget: facebook.com

faceb00k.pw: homograph
facecook.us:  bits
facrbook.com.br: typo
facebook.online: wrongTLD
facebook-fan.de: combo

```

## Set up
```
bash install.sh
```

## APIs

Get squatting type of a domain.
```
python3 squatting_type.py xn--fcebook-8va.com facebook.com
homo

python3 squatting_type.py fcaebook.com facebook.com
typo

python3 squatting_type.py facebook.com google.com
None

python3 squatting_type.py alice-bo.com alice.com
combo
```

Auto scan 100+ popular brands for squatting.
No need to specify the brand domain this time.

Demo:
```
------------------------------------------------------------
python3 squatting_scan.py google-com.org
[google.com, combo]

python3 squatting_scan.py google.tk
[google.com, wrongTLD]

python3 squatting_scan.py facecook.com
[facebook.com, bits]

python3 squatting_scan.py facedook.com
[facebook.com, homo]
```


## Brand Squatting Dataset OpenSource

Squatting_dataset folder contains squatting domains for 766 brands.

We apply our tool for 20 million DNS records.

Format is target-domain, squatting-domain, squatting-dmain in utf8, squatting type, IP

Some records:
```
(u'facebook.com', 'facecook.us.', 'facecook.us', u'bits', '62.149.128.160')
(u'facebook.com', 'xn--fcebook-8va.com.', u'f\xe0cebook.com', u'homo', '199.59.242.150')
(u'github.com', 'ggithub.com.', 'ggithub.com', u'typo', '52.69.166.231')
(u'github.com', 'gtihub.io.', 'gtihub.io', u'typo', '103.224.182.252')
```


## Squatting Methodology

We extend urlcrazy and DNStwist for more efficient squatting detection, by adding a lot of stuff.

URLcrazy-0.5:  https://www.morningstarsecurity.com/research/urlcrazy

DNStwist: https://github.com/elceef/dnstwist

+ increase homograph candidates

+ add combosquatting

+ make name consistent


## Disclaimer and Reference

This is a research prototype, use at your own risk.

If you feel this tool is useful, cite the tool as :dog2: SquatPhish :dog2: is highly appreiciated.


## Acknowledgement

Core contributor: ke tian @ririhedou

Thanks hang hu @0xorz for reproduction testing.

Current version is 0.0.2, updated at June 04 2018