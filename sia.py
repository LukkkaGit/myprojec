import requests
from bs4 import BeautifulSoup

def dajoin(one):
    string = "".join(one)
    return string

mtavari = []

r = requests.get('https://www.rico.ge/ka')
c = r.text
#print(c)
soup = BeautifulSoup(c, 'html.parser')
data = soup.find("tbody")
rows = data.find_all("tr")

for index, row in enumerate(rows,1):
    colums = row.find_all('td')
    valuta = colums[0].text
    sale = colums[1].text
    buy = colums[2].text

    item = [index, valuta, sale, buy]
    mtavari.append(item)

#print(len(mtavari[0]))
usd = (mtavari[0][1]).strip()
usd_buy = float(mtavari[0][2].strip())
usd_sale = float(mtavari[0][3].strip())

eur = mtavari[1][1].strip()
eur_buy = float(mtavari[1][2].strip())
eur_sale = float(mtavari[1][3].strip())

while True:
    op = input("GEL or USD or EUR:")

    if op == "EXIT":  # exit თიშავს
        print("Bye")
        break
    elif op == "exit":
        print("bye bye")
        break
    elif op == "quit":
        print("bye bye bye")
        break
    elif op == "q":
        print("Good Bye")
        break

    gel_count = int(input("Please enter count:"))

    op = op.upper().strip()
    po = list(op)
    mailist = []

    if op.isdigit():
        print("Enter only alphabet")
        continue
    elif op == "":
        print("Enter smth")
        continue

    else:                                            #თუ ასოები და ციფრები არეულია, მარტო ასოებს დაგვიბრუნებს dajoin
        for i in po:
            if not i.isnumeric():
                mailist.append(i)
        l = dajoin(mailist)
        if l == "GEL":
            print(f'You have {gel_count / usd_buy:.2f} USD')
            print(f'You have {gel_count / eur_buy:.2f} EUR')
        elif l == "USD":
            print(f'You have {gel_count * usd_sale:.2f} GEL')
            print(f'You have {gel_count * usd_sale / eur_buy:.2f} EUR')
        elif l == "EUR":
            print(f'You have {gel_count * eur_sale:.2f} GEL')
            print(f'You have {gel_count * eur_sale / usd_buy:.2f} EUR')

    break