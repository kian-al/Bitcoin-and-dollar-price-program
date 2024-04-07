import requests
from bs4 import BeautifulSoup
import re
from collections import OrderedDict
from colorama import Fore
req_bit = requests.get("https://www.tgju.org/profile/crypto-bitcoin")
soup1=BeautifulSoup(req_bit.text,"html.parser")
value1=soup1.find("tbody", attrs={'class': 'table-padding-lg'})  #for now bitcoin price
pattern = r'(\D+)\s+(\d+,\d+)'#for Separating the word from the number
bit_matches=re.findall(pattern,value1.text) #for find word and numbers
bit_dict=OrderedDict()
for match in bit_matches:
    word=match[0]
    numbers=match[1]
    bit_dict[word]=numbers
print(Fore.GREEN+"bitcoin prices :")
for key,value in bit_dict.items():
    print(Fore.WHITE+key, ":", value)
#-------------------------------------------------------------------------------
print(Fore.RED+'-------------------------------------------------------------------------------')
req_usd = requests.get("https://www.tgju.org/profile/price_dollar_rl")
soup2 = BeautifulSoup(req_usd.text, 'html.parser')
value2 = soup2.find("tbody", attrs={'class': 'table-padding-lg'})  # for now dollar to rial price
usd_matches = re.findall(pattern, value2.text)
usd_dict = OrderedDict()
for match in usd_matches:
    word = match[0]
    numbers = match[1]
    usd_dict[word] = numbers
print(Fore.BLUE+'doler to rial price :')
for key, value in usd_dict.items():
    print(Fore.WHITE+key, ":", value)
#--------------------------------------------------------------------------------





