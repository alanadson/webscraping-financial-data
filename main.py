import requests
import bs4
import locale
import tabulate

from models import RealEstateFund, Strategy

locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def percentage_change(percentage_str):
    return locale.atof(percentage_str.split('%')[0])


def decimal_change(decimal_str):
    return locale.atof(decimal_str)


headers = {
    'User-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

answer = requests.get('https://www.fundamentus.com.br/fii_resultado.php', headers=headers)

soup = bs4.BeautifulSoup(answer.text, 'html.parser')

lines = soup.find(id='tabelaResultado').find('tbody').find_all('tr')

result = []

strategy = Strategy(
    price_min=0,
    dividend_yield_min=0,
    p_vp_min=0,
    market_value_min=0,
    liquidity_min=0,
    number_real_min=0,
    average_vacancy_min=0
)

for line in lines:
    data = line.find_all('td')
    paper = data[0].text
    segment = data[1].text
    price = decimal_change(data[2].text)
    ffo_yield = percentage_change(data[3].text)
    dividend_yield = percentage_change(data[4].text)
    p_vp = decimal_change(data[5].text)
    market_value = decimal_change(data[6].text)
    liquidity = decimal_change(data[7].text)
    number_real = int(data[8].text)
    pricer_per_m2 = decimal_change(data[9].text)
    rent_per_m2 = decimal_change(data[10].text)
    cap_rate = percentage_change(data[11].text)
    average_vacancy = percentage_change(data[12].text)

    real_Estate_Fund = RealEstateFund(
        paper, segment, price, ffo_yield, dividend_yield, p_vp, market_value, liquidity, number_real, pricer_per_m2,
        rent_per_m2, cap_rate, average_vacancy
    )

    if strategy.apply_strategy(real_Estate_Fund):
        result.append(real_Estate_Fund)

header = ['PAPER', 'SEGMENT', 'PRICE', 'DIVIDEND YIELD']

table = []

for elements in result:
    table.append([elements.paper, elements.segment, locale.currency(elements.price), f"{locale.str(elements.dividend_yield)}%"])

print(tabulate.tabulate(table, headers=header, tablefmt='fancy_grid'))
