# myapp/tasks.py
from celery import Celery, shared_task
from django.db.models import Q

import json
import os

from .models import UserManager, BankAccount, PhoneVerification, TokenRecord
from .forms import UserCreationForm, EditProfileForm
from web3 import Web3
#celery_app = Celery('store')

app = Celery('website')

@shared_task
def my_periodic_task():
    # Your task logic goes here
    print("Scheduled Task Executed")
    infura = 'https://mainnet.infura.io/v3/' + os.environ.get('INFURA_KEY')
    w3 = Web3(Web3.HTTPProvider(infura))


    # Address of the ERC-721 contract
    contract_address = "0xfFB1641d3148cadb024a6936C43343ad32f9c5a6"

    # ABI of the ERC-721 contract
    contract_abi = [
        {
            "constant": True,
            "inputs": [{"name": "_tokenId", "type": "uint256"}],
            "name": "ownerOf",
            "outputs": [{"name": "owner", "type": "address"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        },
        {
            "constant": True,
            "inputs": [],
            "name": "totalSupply",
            "outputs": [{"name": "", "type": "uint256"}],
            "payable": False,
            "stateMutability": "view",
            "type": "function"
        }
        # ... Add more function definitions as needed ...
    ]

    # Instantiate the contract
    contract = w3.eth.contract(address=contract_address, abi=contract_abi)

    # Get the total supply of tokens
    total_supply = contract.functions.totalSupply().call()

        # Iterate through each token ID and retrieve the owner's address
    for token_id in range(total_supply):
        owner_address = contract.functions.ownerOf(token_id).call()
        token_record = TokenRecord(
            contract_address=contract_address,
            token_id=token_id,  # Replace with the appropriate token ID
            token_owner=owner_address
        )
        token_record.save()
        print("Scheduled Task Executed SAVED")


    pass
