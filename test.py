from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/6e5e803cf1f84b4b85e6533c11f68639'))
print(w3.eth.getBlock('latest'))