# https://docs.open.debank.com/en/reference/api-pro-reference/user#get-user-total-balance-on-all-supported-chains
# https://open.debank.com/admin

import requests

headers = {
    'accept': 'application/json',
    'AccessKey': '9b13f5c9f384962e98c541ef22239bef258c572b',
}

params = {
    'id': '0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE',
}

response = requests.get('https://pro-openapi.debank.com/v1/user/total_balance', params=params, headers=headers)
print(response.content)