from django.contrib import admin
from event.models import Event, Section, Batch, Ticket


class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'banner', 'producer', 'created_at']


class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'section_type', 'created_at']


class BatchAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'expiration_date', 'created_at']


class TicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'ticket_type', 'price', 'amount', 'created_at']


admin.site.register(Event, EventAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Batch, BatchAdmin)
admin.site.register(Ticket, TicketAdmin)
