from django.contrib import admin
from .models import SwiftUser
# Register your models here.

# @admin.register(SwiftUser)
class SwiftUserAdmin(admin.ModelAdmin):
    readonly_fields = ["id"]


admin.site.register(SwiftUser,SwiftUserAdmin)