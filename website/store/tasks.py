# myapp/tasks.py
from celery import Celery, shared_task
from django.db.models import Q

import json

from .models import UserManager, BankAccount, PhoneVerification, TokenRecord
from .forms import UserCreationForm, EditProfileForm
from web3 import Web3
#celery_app = Celery('store')

app = Celery('website')

@shared_task
def my_periodic_task():
    # Your task logic goes here
    print("Scheduled Task Executed")



    pass
