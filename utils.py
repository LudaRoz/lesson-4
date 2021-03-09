from requests import get, utils
from datetime import datetime


def currency_rates(input_code):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    if content.find('<CharCode>' + input_code):
        coin = content.partition('<CharCode>' + input_code)[2]
        if content.find('Value'):
            value = coin.partition('<Value>')[2]
            value = value.partition('</Value>')
            for i in value:
                if i == '':
                    input_code = "None"
                else:
                    input_code = float(value[0].replace(',', '.'))
    data = content.partition("Date=")[2]
    data = data.partition('name')
    data = data[0]
    data = data[1:len(data)-2]
    data = data.replace('.', '-')
    data = datetime.strptime(data, '%d-%m-%Y').date()
    print(input_code, data)
