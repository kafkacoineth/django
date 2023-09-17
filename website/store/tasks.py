# myapp/tasks.py
from celery import Celery, shared_task
from django.db.models import Q

import json

from .models import UserManager, BankAccount, PhoneVerification, TokenRecord
from .forms import UserCreationForm, EditProfileForm

#celery_app = Celery('store')

@shared_task
def my_periodic_task():
    # Your task logic goes here
    print("Scheduled Task Executed")
    token_record = TokenRecord(
        contract_address="Your Contract Address",
        token_id=123,  # Replace with the appropriate token ID
        token_owner="Token Owner Info"
    )
    token_record.save()
    print("Scheduled Task Executed SAVED")
    pass
