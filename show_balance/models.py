from django.db import models
from datetime import datetime

# Create your models here.
class Account(models.Model):
    id = models.IntegerField(primary_key=True)
    owner = models.CharField(max_length=50, default='Jasper')
    name = models.CharField(max_length=50, default='Savings')
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.owner + self.name

class Balance(models.Model):
    id = models.IntegerField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    balance = models.DecimalField(decimal_places=2, max_digits=1E9)
    date = models.DateTimeField()

    def __str__(self):
        return 'balance_' + str(self.id)

class Transaction(models.Model):
    id = models.IntegerField(primary_key=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField()
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)

    def __str__(self):
        return 'transaction_' + str(self.id)
