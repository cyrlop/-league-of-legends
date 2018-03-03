# -*- coding: utf-8 -*-

import re

def rate_pseudo(pseudo):
    pseudo = pseudo.encode('utf-8').strip()

    # Capitalize
    if re.match(r'^[A-Z][a-z]+', pseudo):
        score = 1
    else:
        score = 0.5

    # Number(s)
    if re.match(r'.*\d+.*', pseudo):
        score *= 1.0/2.0
    
    # Special characters
    for c in pseudo:
        if c in "_/*-+:;,?!§$£èé#&":
            score *= 3.0/4.0
        
    return score