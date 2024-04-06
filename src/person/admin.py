from django.contrib import admin
from person.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'role', 'is_active', 'created_at']


admin.site.register(Person, PersonAdmin)
