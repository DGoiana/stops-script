import requests
from seleniumwire import webdriver
from bs4 import BeautifulSoup

def get_bus_data(stop):
  options = webdriver.FirefoxOptions() # can be chrome as well
  options.add_argument("--headless")

  driver = webdriver.Firefox(options=options) # chrome as well
  driver.get(f'https://www.stcp.pt/pt/viajar/horarios/?paragem={stop}&t=smsbus')

  url = "https://www.stcp.pt/pt/itinerarium/"
  driver.get(url)

  token = ''

  for request in driver.requests:
      if "soapclient_b64a55e.php" in request.url and request.response.status_code == 200:
          token = request.url
          break

  driver.quit()

  response = requests.get(token);

  soup = BeautifulSoup(response.text, 'html.parser')

  no_buses = soup.find('div', {'class': 'msgBox warning'})

  if(no_buses):
    print('Sem autocarros nos próximos 60m')
    return 

  table = soup.find('table', {'id': 'smsBusResults'})
  rows = table.find_all('tr')[1:]

  bus_data = []

  for row in rows:
      cols = row.find_all('td')
      if len(cols) == 3:
          line = cols[0].find('a').text.strip()
          time = cols[2].text.strip()

          bus_data.append((line, time))

  for (line, time) in bus_data:
      print(line + ' - ' + time)

if __name__ == "__main__":
    stop = input("Paragem: ")
    print(stop) # ios shortcuts purpose
    get_bus_data(stop)