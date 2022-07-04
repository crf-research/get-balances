#https://docs.etherscan.io/api-endpoints/accounts#get-ether-balance-for-multiple-addresses-in-a-single-call

import time
import requests
import xlsxwriter
import csv

URL = "https://api.etherscan.io/api"

PARAMS = {
    'module': 'account',
    'action': 'balance',
    'address': '0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE',
    'tag': 'latest',
    'apikey': 'JVPJ4F7ED7AHE4UQ9E9MUXP665SS93HHU7'
}

# Get list of addresses - make sure csv is in CSV (MS-DOS) format.
# open('inputfilename.csv', 'r', encoding='utf-8-sig')
with open('export_addresses.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    address_list = list(reader)

# flatten list of lists into list
#list = ["0x3f5ce5fbfe3e9af3971dd833d26ba9b5c936f0be", "0xd551234ae421e3bcba99a0da6d736074f22192ff", "0x564286362092d8e7936f0549571a803b203aaced"]
flat_list = [x for xs in address_list for x in xs]
#print(flat_list)

# Create empty list
balances_list = []
balances_list.append(['Address','ETH'])

counter = 0

# ETHERSCAN
for i in flat_list:
    PARAMS['address'] = i
    r = requests.get(url = URL, params = PARAMS)
    
    # extracting data in json format
    data = r.json()
    
    # convert to int and scale down by 18
    balances_list.append([PARAMS['address'], int(data['result'])/10**18])
    
    counter += 1
    # rate-limit timeout: 5 calls per second | 200 addresses -> 40 seconds
    rate = counter % 5 
    if rate == 0:
        time.sleep(2)

# data we want to write to the worksheet.
balances_tuple = tuple(balances_list)
#print(balances_tuple)

# Workbook() takes one, non-optional, argument which is the filename that we want to create.
workbook = xlsxwriter.Workbook('results.xlsx')

# The workbook object is then used to add new worksheet via the add_worksheet() method.
worksheet = workbook.add_worksheet("balances")

# Start from the first cell. Rows and columns are zero indexed.
row = 0
col = 0
 
# Iterate over the data and write it out row by row.
for address, balance in (balances_tuple):
    worksheet.write(row, col, address)
    worksheet.write(row, col + 1, balance)
    row += 1
 
workbook.close()

print("File exported!")











#r = requests.get(url = URL, params = PARAMS)
#print(r.text)

#https://api.etherscan.io/api ? module=account & action=balance & address=0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE & tag=latest & apikey=JVPJ4F7ED7AHE4UQ9E9MUXP665SS93HHU7

#https://api.etherscan.io/api ? module=account & action=balance & address=0x3f5CE5FBFe3E9af3971dD833D26bA9b5C936f0bE & tag=latest & apikey=JVPJ4F7ED7AHE4UQ9E9MUXP665SS93HHU7