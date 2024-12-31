from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
from djmoney.models.fields import MoneyField


class Token(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    token = models.CharField(max_length=48)
    def __unicode__(self):
        return "{}_token".format(self.user)

class Wallet(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    created_At = models.DateTimeField(default=timezone.now)



class Belonging(models.Model):
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    value = models.IntegerField()
    created_At = models.DateTimeField(default=timezone.now)

class WalletBelongings(models.Model):
    wallet_id = models.ManyToManyField(Wallet)
    belonging_id = models.ManyToManyField(Belonging )


class Cart(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    accNumber = models.PositiveIntegerField(unique=True , validators=[MinValueValidator(999999999999999), MaxValueValidator(10000000000000000)])
    IBAN = models.PositiveBigIntegerField(unique=True , validators=[MinValueValidator(99999999999999999999999), MaxValueValidator(1000000000000000000000000)])
    CVV2 = models.PositiveBigIntegerField(validators=[MinValueValidator(99) , MaxValueValidator(10000)])
    credit = MoneyField(max_digits=14, decimal_places=4,null=True , default_currency='USD')
    created_At = models.DateTimeField(default=timezone.now)




class Expense(models.Model):
    id = models.PositiveIntegerField(unique=True , primary_key=True)
    walletbelongs = models.ForeignKey(WalletBelongings , on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart , null=True , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __unicode__(self):
        return "{}-{}-{}".format(self.date, self.user, self.amount)


class Income(models.Model):
    id = models.PositiveIntegerField(unique=True , primary_key=True)
    walletbelongs = models.ForeignKey(WalletBelongings , on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart , null=True , on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __unicode__(self):
        return "{}-{}-{}".format(self.date, self.user, self.amount)




class Passwordresetcodes(models.Model):
    code = models.CharField(max_length=32)
    email = models.CharField(max_length=120)
    time = models.DateTimeField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)




# Create your models here.
