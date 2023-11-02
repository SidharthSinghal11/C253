
from web3 import Web3
import time
 

ganache_url = 'http://127.0.0.1:7545'

web3_ganache_connection = Web3(Web3.HTTPProvider(ganache_url))

Alice_account = '0x06136A586cfca61a2c1a496Ac5f5313c59EC4Cc7'
James_account = '0xbcA2E219E14f7A5b1E0f683cCb17125A7797AA3E'
Ryan_account  = '0x9a07C21254A46399D7c23b2bDb5C41e1c3016a02'


nonce1 = web3_ganache_connection.eth.get_transaction_count(Alice_account)

transaction_data1 = {
	'nonce':nonce1,
	'to':James_account,
	'value':web3_ganache_connection.to_wei(5, 'ether'),
	'gas':21000,
	'gasPrice':web3_ganache_connection.to_wei(50,'gwei')
}

private_key1 = '0x78123a44dc6595fa32250e60e14246114e3e33261e4103873f83f72df7091ef5'

singed_transaction1 = web3_ganache_connection.eth.account.sign_transaction(transaction_data1,private_key1)
transaction_hash1 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction1.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash1))




print("Wait for few seconds transaction is in progress...") 
time.sleep(5)



nonce2 = web3_ganache_connection.eth.get_transaction_count(James_account)

transaction_data2 = {
	'nonce':nonce2,
	'to':Ryan_account,
	'value':web3_ganache_connection.to_wei(2, 'ether'),
	'gas':21000,
	'gasPrice':web3_ganache_connection.to_wei(40,'gwei')
}

private_key2 = '0x7ba58e7c9a2e0546d29f81a20cfc379f9be29b9829ab4663bd17af92d3830a6f'

singed_transaction2 = web3_ganache_connection.eth.account.sign_transaction(transaction_data2,private_key2)
transaction_hash2 = web3_ganache_connection.eth.send_raw_transaction(singed_transaction2.rawTransaction)

print(web3_ganache_connection.to_hex(transaction_hash2))



