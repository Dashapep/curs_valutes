import requests
import sys

response = requests.get("https://api.exchangeratesapi.io/{}".format(sys.argv[1]))
if response:
    json_response = response.json()
    print("curs {} on {} = ".format(sys.argv[2], sys.argv[1]) + str(json_response["rates"][sys.argv[2]]))
# python main.py 2020-02-02 RUB