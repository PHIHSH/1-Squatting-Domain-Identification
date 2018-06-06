import sys

import utils
import squatting_type


def get_type(test):
    '''
    'wrongtld', 'combo', 'typo', 'bits', 'homo', 'other'
    '''

    results = []

    if test.endswith('.'):
        test = test[:-1]

    if 'xn--' in test:
        test = utils.decode_punycode(test)
    
    for brand in utils.SQUAT_D:
        squatting_dict = utils.SQUAT_D[brand]

        brand_domain, brand_tld = utils.get_domain_tld(brand)

        if len(brand_domain) <= 3:
            continue
        
        t = squatting_type.get_label(test, squatting_dict, brand)
        if t:
            results.append([brand, t])
   
    return results


if __name__ == "__main__":
    test = sys.argv[1]
    print(get_type(test))