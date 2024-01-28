# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 20:23:01 2024

@author: rubar
"""

#İf For ve Fonksiyonların birlikte kullanımı

#Maaşı 3000 tlden az olanlara %20 zam maaşı 3000 tlden fazla
#olanlara %10 zam

maaslar = [1000,1500,2000,2500,3000,3500,4000,4500,5000]

def yuzde_on(x):
    return (x* 10/100 + x)
yuzde_on(100)

def yuzde_yirmi(x):
    return (x* 20/100 + x)
yuzde_yirmi(200)

for i in maaslar:
    if i >= 3000:
        yuzde_on(i)
    else:
        yuzde_yirmi(i)


 
    
 
    
 
    
 
    
 
    
 
    
 
    
 
    