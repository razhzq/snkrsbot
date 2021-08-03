# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 15:49:09 2021

@author: Loga
"""

from sneaker11function import *

try:
    login()
    delivery_add()
    payment_card()
except:
    payment_card()
    pass
finally:
    consent_status()
    

Submit().sd()