#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import idna
import tldextract

import SQUT_DIC

EDIT_DISTANCE_THRESHOLD = 2
HYPHEN_DISTANCE_THRESHOLD = 4
DOMAIN_LENGTH_THRESHOLD = 20


############################# PUNY CODE ANd EXTRACT #####################

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


def _domain_tld_with_tldextract(domain_tld):
    ext = tldextract.extract(domain_tld)

    if ext.subdomain:
        domain = ext.subdomain + u'.' + ext.domain
    else:
        domain = ext.domain

    return domain, ext.suffix


def is_same_domain_and_tld_ignore_subdomain(input_domain_tld, original_domain, original_tld):
    ext = tldextract.extract(input_domain_tld)
    domain = ext.domain
    myTLD = ext.suffix
    if domain == original_domain and original_tld == myTLD:
        return True
    return False

################# FINE GRAINED MATCHING ################
def labeling_candidiates(input_domain_tld, squat_dict, original_domain, original_tld):
    try:
        # domain, tld = __domain_tld(input_domain_tld)
        # original_domain, original_tld = __domain_tld(original_domain_tld)
        domain, tld = _domain_tld_with_tldextract(input_domain_tld)

        if is_same_domain_and_tld_ignore_subdomain(input_domain_tld, original_domain, original_tld):
            return False

        if wrong_tld_squatting(domain, tld, original_domain, original_tld):
            return u'wrongTLD'

        if mobile_phishing_via_padding(domain, original_domain):
            return u'mobilePhishing'

        key = typo_homo_bits_others_squatting(domain, squat_dict)
        if key:
            return key

        if combo_squatting_detection(domain, original_domain):
            return u'combo'

        #if combo_squatting_detection_nohyphen(domain, original_domain):
        #    return (u'combo-nohyphen')
        # i do not use this, but you can use


        # key2 = edit_distance_is_small_than_1(domain, original_domain)
        # if key2:
        #    return key2

        return False

    except:
        f = open('log-error.log', 'a')
        f.write(input_domain_tld)
        f.write('\n')
        f.flush()
        f.close()


def wrong_tld_squatting(candidate_domain, tld, original_domain, original_tld):
    if (candidate_domain == original_domain) and (tld != original_tld):
        return True
    return False


def combo_squatting_detection(domain, original_domain):
    # combo = u'combo'

    combo1 = u'-' + original_domain
    combo2 = original_domain + u'-'

    if (combo1 in domain) or (combo2 in domain):
        return True
    return False


def combo_squatting_detection_nohyphen(domain, original_domain):
    if original_domain in domain:
        return True
    return False


def typo_homo_bits_others_squatting(domain, squat_dic):
    """
    typo = u'typo'
    bit = u'bits'
    homo = u'homo'
    other = u'other'
    """
    for key in squat_dic:
        current_type = squat_dic[key]
        if domain in current_type:
            return key
            # for item in current_type:
            #    if item == domain:
            #        return key

    return None


def mobile_phishing_via_padding(domain, original_domain):
    def count_continous_hypens(domain):
        count = 0
        for i in domain:
            if i == u'-':
                count += 1
                if count > HYPHEN_DISTANCE_THRESHOLD:
                    return True
            else:
                count = 0
        if count > HYPHEN_DISTANCE_THRESHOLD:
            return True
        return False

    if original_domain in domain and count_continous_hypens(domain):
        return True
    return False


######################## MAIN API ##################
def squating_type(domain_tld):
    """
    example: facebook.com
    """
    results = []

    qname = domain_tld

    if qname.endswith(u'.'):
        qname = qname[:-1]

    if u'xn--' in qname:
        qname = decode_punycode(qname)
    
    match = 0
    for brand in SQUT_DIC.SQUAT_D:
        squat_dict = SQUT_DIC.SQUAT_D[brand]
        original_domain, original_tld = _domain_tld_with_tldextract(brand)
        if len(original_domain) <= 3:
            continue
        t = labeling_candidiates(qname, squat_dict, original_domain, original_tld)
        if t:
            results.append([domain_tld, brand, t])
            print ("[Detection] [{}] -> [{}] -> [{}]".format(domain_tld, brand, t))
            match = 1

    if match == 0:
        print ("[NOMatch] {}".format(domain_tld))
    return results


if __name__ == "__main__":
    scan = sys.argv[1]
    squating_type(scan)