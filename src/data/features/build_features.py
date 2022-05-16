import numpy as np
import pandas as pd
import tldextract
from collections import Counter


def chr_count_FQN(url):
    chr_sum= 0
    for i in url:
        if i==".":  
            continue
        else: 
            chr_sum += 1
    return chr_sum
  
def sub_domain_count(url):
    sub_domain, _ , __ =tldextract.extract(url)
    return chr_count_FQN(sub_domain)

def upper_count(url):
    up_sum = 0
    for i in url:
        if i.isupper():
            up_sum += 1
    return up_sum

def lower_count(url):
    low_sum = 0
    for i in url:
        if (i.islower()==True) and (i.isdigit()==False):
            low_sum += 1
    return low_sum
    
def numeric_count(url):
    num_sum = 0
    for i in url:
        if i.isnumeric():
            num_sum += 1
    return num_sum        

def entropy_count(url):
    pb, lenn = Counter(url), float(len(url))
    return - sum( count/lenn * np.log2(count/lenn) for count in pb.values())

def chr_special_count(url): 
    special_sum= 0
    for i in url:
        if (i.isalpha()) or (i.isdigit() or i == '.'):
            continue
        else: 
            special_sum += 1
    return special_sum

def label_count(url):
    l_sum =len(url.split('.'))
    return l_sum

def label_max(url):
    labels = url.split('.')
    return max(([len(x) for x in labels]))

def label_avg(url):
    labels = url.split('.')
    return np.average(([len(x) for x in labels]))
    
def longest_word(url):
    l_word = label_max(url)
    lens = [len(x) for x in url.split('.')]
    return url.split('.')[lens.index(max(lens))]
    
def second_level_D(url):
    subdomain,sld_,suffix_=tldextract.extract(url)
    return  sld_ 
    
def contains_subdomain(url):
    subdomain,sld_,suffix_=tldextract.extract(url)
    if len(subdomain) > 0:
        return 1
    else :
        return 0
        
def sub_domain_len(url):
    subdomain,sld,suffix_=tldextract.extract(url)
    return chr_count_FQN(subdomain)+chr_count_FQN(sld)        
    
def build_feature_df(url):
    dictt = {'FQDN_count': chr_count_FQN(url),
            'subdomain_length': sub_domain_count(url),
            'upper': upper_count(url),
            'lower': lower_count(url),
            'numeric': numeric_count(url),
            'entropy': entropy_count(url),
            'special': chr_special_count(url),
            'labels': label_count(url),
            'labels_max': label_max(url),
            'labels_average': label_avg(url),
            'longest_word': longest_word(url),
            'sld': second_level_D(url),
            'len': sub_domain_len(url),
            'subdomain': contains_subdomain(url)
           }
    
    df = pd.DataFrame(dictt, index=[1])
    return df