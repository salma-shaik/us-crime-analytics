import requests
import json


base_url = 'https://api.census.gov/data/2000/sf3'
list1 = 'P043001,P082001,PCT035001,PCT035002,PCT035003,PCT035010,PCT035017'

# print(f'list o fvars is {list1}')


url = f'{base_url}?get={list1},NAME&for=county:001&in=state:01&key=d2b9b07dfed3cc16bbb93f03b445c16a4fed0c72' # 3140 calls
response = requests.get(url)

resp = json.loads(response.content)

print(resp)