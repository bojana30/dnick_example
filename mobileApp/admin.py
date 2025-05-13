from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import MobilePhone, Manufacturer


class MobilePhoneAdmin(admin.ModelAdmin):
    exclude = ['user']  # Скрие го полето од формата

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(MobilePhoneAdmin, self).save_model(request, obj, form, change)


admin.site.register(MobilePhone, MobilePhoneAdmin)
admin.site.register(Manufacturer)
