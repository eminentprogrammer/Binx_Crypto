import requests



def format_currency(value):
    return "₦{:,.2f}".format(value)

url = "http://44.226.122.3/get_banks/"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
    "content-type": "application/json",
}

res = requests.get(url, headers).json()

print(res)