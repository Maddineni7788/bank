from django.contrib import admin
from bankingapp.models import Account,Register, AccountDetails, BankAccount, Transaction, Withdrawal, Deposit, UserProfile,Cashier

# Register your models here.
admin.site.register(Register)
admin.site.register(AccountDetails)
admin.site.register(BankAccount)
admin.site.register(Transaction)
admin.site.register(Withdrawal)
admin.site.register(Deposit)
admin.site.register(UserProfile)
admin.site.register(Cashier)
admin.site.register(Account)

# Register your models here.
