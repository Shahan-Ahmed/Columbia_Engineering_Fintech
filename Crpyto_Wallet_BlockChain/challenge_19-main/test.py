# Imports
import os
from dotenv import load_dotenv
load_dotenv()
from bip44 import Wallet
from web3 import Account
from web3 import Web3
w3 = Web3(Web3.HTTPProvider('HTTP://127.0.0.1:7545'))



mnemonic = os.getenv("MNEMONIC")
print(mnemonic)


