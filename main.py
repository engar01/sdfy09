import requests
from bs4 import BeautifulSoup


class CurrencyConverter:
    def __init__(self, url):
        self.data = self.get_data(url)

    def get_data(self, url):
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup

    def convert(self, amount):
        usd_rate = None
        for td in self.data.find_all('td', class_="value-name"):
            if td.find('a').text.strip() == "Долар США":
                usd_rate = float(td.find_next_sibling('td').text.strip().replace(',', '.'))
                break
        return round(amount / usd_rate, 2)


def main():
    url = 'https://bank.gov.ua/markets/exchangerates'
    converter = CurrencyConverter(url)
    amount = float(input("Enter amount in your currency: "))
    usd_amount = converter.convert(amount)
    print(f"{amount:.2f} UAH is equal to {usd_amount:.2f} USD.")


if __name__ == '__main__':
    main()
