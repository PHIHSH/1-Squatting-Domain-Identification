import idna
import csv
import tldextract

def decode_punycode(label):
    """helper function; decodes a section of the netloc from punycode."""
    try:
        return idna.decode(label.encode('ascii'))
    except UnicodeError:
        pass
    except ValueError as exc:
        # see https://github.com/john-kurkowski/tldextract/issues/122
        # if "narrow Python build" in exc.args[0]:
        # warnings.warn("can not decode punycode: %s" % exc.args[0], UnicodeWarning, stacklevel=2)
        pass
        # return label
        # raise
    return label


def get_domain_tld(full_domain):
    ext = tldextract.extract(full_domain)

    if ext.subdomain:
        domain = ext.subdomain + '.' + ext.domain
    else:
        domain = ext.domain

    return domain, ext.suffix


def logging(message):
    with open('logging.csv', 'a') as fileobj:
        writer = csv.writer(fileobj)
        writer.writerow(message)