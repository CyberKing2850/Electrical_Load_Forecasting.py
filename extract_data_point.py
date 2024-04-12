import requests
from bs4 import BeautifulSoup


def extract_data_point():
    url = 'https://www.delhisldc.org/Redirect.aspx?Loc=0804'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    states = ['Chandigarh', 'Haryana', 'J & K', 'Punjab', 'Rajasthan']
    load_values = {}
    element = soup.find(id='ContentPlaceHolder3_Dstatedrawl')

    def extract_data(td):
        font = td.find("font")
        b = font.find("b")
        return b.text

    result = ""
    rows = element.find_all("tr")
    for tr in rows[1:]:
        tds = tr.find_all("td")
        result+=( extract_data(tds[0]))
        result+=(",")
        result+=( extract_data(tds[-1]))
        result+=("\n")
    return result

# print(extract_data_point())
