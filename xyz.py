import requests
import bs4
from prettytable import PrettyTable
name=list()
code=list()
spo=list()
n=input("Enter the numbers of users: ")
x=PrettyTable()
coder=list()
spojr=list()
total=list()

def codechef(user):
    p="https://codechef.com/users/"
    r=user
    q=p+r
    res=requests.get(q)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    coder.append(len(soup.article.getText().split())-1)
    return;

def spoj(user):
    p="https://spoj.com/users/"
    r=user
    q=p+r
    res=requests.get(q)
    soup=bs4.BeautifulSoup(res.text,'html.parser')
    spojr.append((int(soup.dd.getText())))

    return;

for i in range(int(n)):
    na=input("\nUsername :")
    name.append(na)
    p=input("Codechef handle :")
    code.append(p)
    q=input("SPOJ handle :")
    print("\nWait till the data is scraped!")
    spo.append(q)
    codechef(p)
    spoj(q)
    total.append(coder[i] + spojr[i])
    
    
x=PrettyTable(["name","codechef handle","spoj handle","codechef questions","spoj questions","total questions"])
for i in range(0,(int)(n)):
    x.add_row([name[i],code[i],spo[i],coder[i],spojr[i],total[i]])
print(x.get_string(sortby=("total questions"), reversesort=True))




    
