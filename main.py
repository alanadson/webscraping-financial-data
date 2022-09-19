import requests
import bs4
import tabulate

headers = {'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

answer = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)

soup = bs4.BeautifulSoup(answer.text, 'html.parser')

print(soup.prettify())

lines = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

for line in lines:
    data = line.find_all('td')
    print(
        f"[{data[0].text}]\n"
        f"Cotação: {data[2].text}\n"
        f"Setor: {data[1].text}\n"
        f"DY %: {data[4].text}\n"
        f"P/VP: {data[5].text}\n"
    )
