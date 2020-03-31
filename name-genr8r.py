from random import randint
import requests
import warnings
warnings.filterwarnings("ignore")

def get_rand_element(lst):
    l = len(lst)
    return lst[randint(0, l-1)]

def get_availibilty(name):
    url = "http://in.godaddy.com/domainsapi/v1/search/exact?q=" + name + "&key=dpp_search&pc=&ptl="
    r = requests.get(url, verify = False)
    r_json = r.json()
    #print(r_json)
    return_str = ""
    if "ExactMatchDomain" in r_json:
        if "IsAvailable" in r_json["ExactMatchDomain"] and r_json["ExactMatchDomain"]["IsAvailable"]:
            return_str += "Available, "
        if "IsPremiumTier" in r_json["ExactMatchDomain"] and r_json["ExactMatchDomain"]["IsPremiumTier"]:
            return_str += "Premium, "
    if "Products" in r_json:
        pass
        # return_str += str(r_json["Products"][0]["PriceInfo"]["CurrentPriceDisplay"]) +  ", "

    return name + ", " + return_str[:-2]

vowels_list = ['a','e','i','o','u']
consonants_list = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

for x in range(1):
    print("testing tab to spaces switch")


for _ in range(200):
    print(get_availibilty(get_rand_element(consonants_list) + get_rand_element(vowels_list) + get_rand_element(consonants_list) + get_rand_element(vowels_list) + get_rand_element(consonants_list)))
