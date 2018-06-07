from squatting.CONSTANTS_homo_mapping import HOMO_MAP_UNICODE
from squatting.dnsTwist_squatting import get_squatting_domains_dict_from_dnstwist
from squatting.urlCrazy_squatting import get_domains_from_url_crazy

import tldextract


def get_squatting_dict(domain_name, base_domain=None):
    """
    :param domain_name: e.g., facebook.com
    :return:
    """
    dict_crazy = get_domains_from_url_crazy(domain_name)
    dict_dnsTwist = get_squatting_domains_dict_from_dnstwist(domain_name)
    for i in dict_dnsTwist:
        dict_crazy[i].extend(dict_dnsTwist[i])
        dict_crazy[i] = list(set(dict_crazy[i]))

    if base_domain is None:
        ext = tldextract.extract(domain_name)
        if ext.subdomain:
            domain = ext.subdomain + u'.' + ext.domain
        else:
            domain = ext.domain

        base_domain = domain

    for i in dict_crazy:
        key = list(set(dict_crazy[i]))
        if base_domain in key:
            key.remove(base_domain)
        dict_crazy[i] = key

    return dict_crazy
    # a complete dict of all the typo/bits/homograph squatting domains


if __name__ == "__main__":
    test_domain = 'faceboook.com'
    d = get_the_complete_list_of_squatting_domains(test_domain)
    import pprint
    pprint.pprint(dict(d), indent=1)