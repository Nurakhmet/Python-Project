from django.contrib import admin
from .models import User, Catalogue, Order, Account
# Register your models here.
admin.site.register(User)
admin.site.register(Catalogue)
admin.site.register(Order)
admin.site.register(Account)

