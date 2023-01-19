from django.contrib import admin

from products.admin import BasketAdmin
from users.models import User, EmailVerification


# Register your models here.
# admin.site.register(User)

@admin.register(User)
class UserAdmon(admin.ModelAdmin):
    list_display = ('username',)
    inlines = (BasketAdmin,)


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ('code', 'user', 'expiration')
    fields = ('code', 'user', 'expiration', 'created')
    readonly_fields = ('created',)
