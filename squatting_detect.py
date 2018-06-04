#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ketian'
__version__ = '1.04b'
__email__ = 'ririhedou@gmail.com'

import idna
import tldextract
from squatting.complete_squatting import get_the_complete_list_of_squatting_domains

EDIT_DISTANCE_THRESHOLD = 2
HYPHEN_DISTANCE_THRESHOLD = 4
DOMAIN_LENGTH_THRESHOLD = 20


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


################# FINE GRAINED MATCHING ################
def labeling_candidiates(input_domain_tld, squat_dict, target_domain_tld):
    try:
        domain, tld = _domain_tld_with_tldextract(input_domain_tld)
        original_domain, original_tld = _domain_tld_with_tldextract(target_domain_tld)

        if wrong_tld_squatting(domain, tld, original_domain,original_tld):
            return 'wrongTLD'

        #if mobile_phishing_via_padding(domain,original_domain):
        #    return 'mobilePhishing'

        if combo_squatting_detection(domain, original_domain):
            return 'combo'

        key = typo_homo_bits_others_squatting(domain, squat_dict)
        if key:
            return key

        #key2 = edit_distance_is_small_than_1(domain, original_domain)
        #if key2:
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


def combo_squatting_detection(domain,original_domain):
    combo1 = u'-'+original_domain
    combo2 = original_domain+u'-'

    if (combo1 in domain) or (combo2 in domain):
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
        for item in  current_type:
            if item == domain:
                return key

    return None


# ################# NOT USED THE FOLLOWING      ##############
'''
def edit_distance_is_small_than_1(domain, original_domain):
    # a small edit-distance
    #TODO this is the last step, if we did not find any match
    distance = editdistance.eval(domain, original_domain)
    if distance <= 1:
        return u'other'
    return False
'''
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


def get_squatting_type_by_compare_target_brand(target_domain_tld, squatting_domain_tld):
    qname = squatting_domain_tld

    if qname.endswith(u'.'):
        qname = qname[:-1]

    if u'xn--' in qname:
        qname = decode_punycode(qname)

    squatting_dict = get_the_complete_list_of_squatting_domains(target_domain_tld)
    t = labeling_candidiates(qname, squatting_dict, target_domain_tld)
    if t:
        print ("{} is a {} of {}".format(squatting_domain_tld,t,target_domain_tld))
    else:
        print ("Do not find the match")



if __name__ == "__main__":

    sq_f = "xn--fcebook-8va.com"
    target = "facebook.com"

    sq_f = "tianke.com"
    target = "tianke.org"

    get_squatting_type_by_compare_target_brand(target, sq_f)