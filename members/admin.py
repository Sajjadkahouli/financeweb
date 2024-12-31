from django.contrib import admin
from .models import *


admin.site.register(Expense)
admin.site.register(Income)
admin.site.register(Token)
admin.site.register(Cart)
admin.site.register(WalletBelongings)
admin.site.register(Belonging)
admin.site.register(Wallet)

# Register your models here.
