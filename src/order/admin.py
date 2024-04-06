from django.contrib import admin
from order.models import Order, DiscountCoupon, Payment


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'created_at']


class DiscountCouponAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'percentage', 'expiration_date', 'created_at']


class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'created_at']


admin.site.register(Order, OrderAdmin)
admin.site.register(DiscountCoupon, DiscountCouponAdmin)
admin.site.register(Payment, PaymentAdmin)
