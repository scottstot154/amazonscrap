import requests
from bs4 import BeautifulSoup

header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
source = requests.get('https://www.amazon.in/s?bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc&qid=1624216249&rnid=3837712031&ref=lp_976420031_nr_p_89_3',headers=header)
soup = BeautifulSoup(source.content, 'html.parser')

names = soup.find_all('span', class_="a-size-base-plus a-color-base a-text-normal")
price = soup.find_all('div', class_="a-row a-size-base a-color-base")
ratings = soup.find_all('div', class_="a-row a-size-small")
delivery = soup.find_all('div', class_="a-row s-align-children-center")


nl = []
for name in names:
    nl.append(name.text)

pl = []
for pri in price:
    pl.append(pri.text.split('₹')[1])

rl = []
for rating in ratings:
    rl.append(rating.text.split( )[0])
    
dl = []
for deli in delivery:
    dl.append(deli.text.split(', ')[1])

print(len(nl))
for j in range(len(pl)):
    pl[j] = pl[j].replace(',','')

for k in range(len(nl)):
    nl[k] = nl[k].replace("&","and")

for i in range(len(nl)-1):
    requests.get("http://127.0.0.1:8000/products/?name="+nl[i]+"&price="+pl[i]+"&rating="+rl[i]+"&delivery="+dl[i])
    print('done',i)


