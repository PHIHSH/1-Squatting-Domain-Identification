import datetime
import sys

import utils
from squatting.complete_squatting import get_squatting_dict


def get_type(test, target):
    '''
    'wrongtld', 'combo', 'typo', 'bits', 'homo', 'other'
    '''

    if test.endswith('.'):
        test = test[:-1]

    if 'xn--' in test:
        test = utils.decode_punycode(test)

    # print(test, target)
    squatting_dict = get_squatting_dict(target)
    t = get_label(test, squatting_dict, target)

    return t if t else None


def get_label(test, squatting_dict, target):
    test_domain, test_tld = utils.get_domain_tld(test)
    target_domain, target_tld = utils.get_domain_tld(target)

    if is_wrongtld(test_domain, test_tld, target_domain, target_tld):
        return 'wrongtld'

    if is_combo(test_domain, target_domain):
        return 'combo'

    key = is_homo_bits_others(test_domain, squatting_dict)
    if key:
        return key

    return False


def is_wrongtld(test_domain, test_tld, target_domain, target_tld):
    if test_domain == target_domain and test_tld != target_tld:
        return True
    return False


def is_combo(test_domain, target_domain):
    combo1 = '-' + target_domain
    combo2 = target_domain + '-'

    if combo1 in test_domain or combo2 in test_domain:
        return True
    return False


def is_homo_bits_others(test_domain, squatting_dict):
    for key in squatting_dict:
        if test_domain in squatting_dict[key]:
            return key
    return None


if __name__ == "__main__":
    # sq_f = "xn--fcebook-8va.com"
    # target = "facebook.com"

    test = sys.argv[1]
    target = sys.argv[2]

    print(get_type(test, target))
