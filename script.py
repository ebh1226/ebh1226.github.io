import requests
import json
api_key='pfMb9y5mDNML68G-FPoXUNIFOfld8FcVEUiytLyAtlasz_csKKBPUtL7ykVND7LN9a_AyAuU_OfsDuVpZcwcuMZoNzoVPmIF7n3ZYto7Z-0ewU5zN0-7teSTvvdvYXYx'
headers = {'Authorization': 'Bearer %s' % api_key}
url='https://api.yelp.com/v3/business/search'
params = {'term':'mexican','location':'Charlottesville'}
req=requests.get(url, params=params, headers=headers)
print('The status code is {}'.format(req.status_code))
json.loads(req.text)