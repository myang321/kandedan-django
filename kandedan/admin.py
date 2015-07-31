from django.contrib import admin

# Register your models here.
from .models import Users, Groups, Transaction, Trans_detail, Balance

admin.site.register(Users)
admin.site.register(Groups)
admin.site.register(Transaction)
admin.site.register(Trans_detail)
admin.site.register(Balance)
