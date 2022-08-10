import requests
import json

print("Welcome to Gaft v1.0.0. Developed by Koky and Sully")

rentalprice = int(input("How much are you looking to pay?"))


def getListing():
    headers = {
    'Host': 'gateway.daft.ie',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
    'platform': 'iOS',
    'Accept': 'application/json',
    'brand': 'daft',
    'Accept-Language': 'en-GB,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Daft.ie/0 CFNetwork/1335.0.3 Darwin/21.6.0'
    }
    url = "https://gateway.daft.ie/old/v1/listings"
    data = '{"section":"residential-to-rent","geoFilter":{"storedShapeIds":["33"],"name":"location","geoSearchType":"STORED_SHAPES","mapView":false},"filters":[{"values":["published"],"name":"adState"}],"paging":{"pageSize":25},"ranges":[{"name":"rentalPrice","to":"2000","from":""}],"sort":"bestMatch"}'

    response = requests.post(url, headers=headers, data=data)
    jsonresp = response.json()
    listings = jsonresp['listings']

    for x in listings:
        print('Listing ID:' + ' ' + str(x['listing']['id']) + ' Price: ' + x['listing']['price'])

getListing()

def sendEmail():
    