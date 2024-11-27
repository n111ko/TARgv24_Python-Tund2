from datetime import *
from calendar import *
from random import *
#import math
from math import *

# tana=date.today() #nimetus() - funktsioon
# tanaf=date.today().strftime("%B %d, %Y")

# print(f"Tere!, Täna on {tanaf}")
# d=tana.day #nimetus - omadus
# m=tana.month
# y=tana.year

# print(d)
# print(m)
# print(y)

####################################################

# print("Tere tulemast!")
# nimi=input("Mis on sinu nimi? ").capitalize() #lower()-aaa,upper()-AAA,capitalize()-Aaa
# print("Tere tulemast! Tervitan sind ", nimi) 
# print("Tere tulemast! Tervitan sind "+ nimi)
# try:
#     vanus=int(input("Kui vana sa oled?"))
#     print("Tere tulemast! Tervitan sind "+nimi+" Sa oled ",vanus,"aastat vana")
#     print(f"\tTere tulemast! \nTervitan sind {nimi} Sa oled {vanus} aastat vana")
# except:
#     print("On vaja numbreid sisestada!")

#####################################################





## Ulesanne 2 ##

# vastus1=3+8/(4-2)*4
# vastus2=3+8/4-2*4
# vastus3=(3+8)/(4-2)*4
# vastus4=round((3+8)/(4-2)*4)

# print(vastus1, "\n", vastus2, "\n", vastus3, "\n", vastus4)

################



# Ulesanne 3 ##

#1 variant
# try:
#     r=int(input("Ruudu sees asub ring. Ringi raadius on R. Sisesta R: "))
#     ruudu_pindala=4*r**2
#     ruudu_umbermoot=4*r
#     ringi_pindala=math.pi*r
#     ringi_umbermoot=math.pi*2*r
      
#     print(f"Ringi pindala on {ringi_pindala}\nRingi ümbermõõt on {ringi_umbermoot}\nRuudu pindala on {ruudu_pindala}\nRuudu ümbermõõt on {ringi_umbermoot}\n")

#     # print(ruudu_pindala)
#     # print(ruudu_umbermoot)
#     # print(ringi_pindala)
#     # print(ringi_umbermoot)
# except:
#     print("On vaja numbreid sisestada!")

#2 variant
# R=round(random()*100) #0.0...1.0
# print(f"R={R}")
# ruudu_pindala=4*R**2
# ruudu_umbermoot=4*R
# ringi_pindala=math.pi*R
# ringi_umbermoot=math.pi*2*R

# print(f"Ringi pindala on {ringi_pindala}\nRingi ümbermõõt on {ringi_umbermoot}\nRuudu pindala on {ruudu_pindala}\nRuudu ümbermõõt on {ringi_umbermoot}\n")

###############



## Ulesanne 4 ##

d=2.575 # mündi d
maa=6378 # maa radius km
maa*=100000 # maa radius sm
Lmaa=2*pi*maa
kogus=int(Lmaa/d)
print(f"On vaja {kogus} mündi.\nMeil on vaja {kogus*2} eur")