from urllib.request import urlopen as uRaq
from bs4 import BeautifulSoup as soup

quotes_page='https://bluelimelearning.github.io/my-fav-quotes/'


uClient=uRaq(quotes_page)
page_html=uClient.read()
uClient.close()
page_soup=soup(page_html,'html.parser')
quotes=page_soup.findAll('div',{'class':'quotes'})


for quote in quotes:
    fav_qote=quote.findAll('p',{'class':'aquote'})
    aquote=fav_qote[0].strip()

    fav_author=quote.findAll('p',{'class':'author'})
    author=fav_author[0].strip()

    print(aquote)
    print(author)

