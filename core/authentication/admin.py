from django.contrib import admin
from .models import (
    User, Role, UserRole, Category, Product, ProductAttribute, Order, 
    OrderDetail, Cart, CartItem, Payment, Supplier, Inventory, Review, 
    Wishlist, WishlistItem, Discount, OrderDiscount, AuditLog, Return, 
    Exchange, Subscription, Notification, OTP
)
@admin.register(OTP)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('otp', 'email', 'created_at', 'expires_at')
    # search_fields = ('phone_number', 'company_name', 'city', 'gst_number', 'registration_number')

@admin.register(User)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'company_name', 'city', 'postal_code', 'gst_number', 'registration_number')
    search_fields = ('phone_number', 'company_name', 'city', 'gst_number', 'registration_number')

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role_name', 'description')
    search_fields = ('role_name',)

@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    search_fields = ('user__phone_number', 'role__role_name')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'parent_category', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('created_at', 'updated_at')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock_quantity', 'category', 'brand', 'model_number', 'warranty_period', 'created_at', 'updated_at')
    search_fields = ('name', 'brand', 'model_number', 'category__name')
    list_filter = ('created_at', 'updated_at', 'category')

@admin.register(ProductAttribute)
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('product', 'attribute_name', 'attribute_value')
    search_fields = ('product__name', 'attribute_name')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'status', 'total_amount', 'shipping_method', 'payment_method', 'created_at', 'updated_at')
    search_fields = ('user__phone_number', 'status', 'shipping_method', 'payment_method')
    list_filter = ('created_at', 'updated_at', 'status')

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price', 'discount', 'total_price')
    search_fields = ('order__user__phone_number', 'product__name')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__phone_number',)
    list_filter = ('created_at', 'updated_at')

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'added_at')
    search_fields = ('cart__user__phone_number', 'product__name')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'payment_date', 'amount', 'payment_method', 'transaction_id', 'payment_status')
    search_fields = ('order__user__phone_number', 'transaction_id', 'payment_method')
    list_filter = ('payment_date', 'payment_status')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_name', 'contact_email', 'contact_phone', 'created_at', 'updated_at')
    search_fields = ('name', 'contact_name', 'contact_email', 'contact_phone')
    list_filter = ('created_at', 'updated_at')

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'stock_level', 'reorder_level', 'last_restocked', 'created_at', 'updated_at')
    search_fields = ('product__name', 'supplier__name')
    list_filter = ('last_restocked', 'created_at', 'updated_at')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'comment', 'created_at')
    search_fields = ('product__name', 'user__phone_number', 'rating')
    list_filter = ('created_at', 'rating')

@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    search_fields = ('user__phone_number',)
    list_filter = ('created_at', 'updated_at')

@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ('wishlist', 'product', 'added_at')
    search_fields = ('wishlist__user__phone_number', 'product__name')

@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('code', 'description', 'discount_amount', 'start_date', 'end_date', 'is_active')
    search_fields = ('code', 'description')
    list_filter = ('start_date', 'end_date', 'is_active')

@admin.register(OrderDiscount)
class OrderDiscountAdmin(admin.ModelAdmin):
    list_display = ('order', 'discount')
    search_fields = ('order__user__phone_number', 'discount__code')

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'action', 'details', 'timestamp')
    search_fields = ('user__phone_number', 'action')
    list_filter = ('timestamp',)

@admin.register(Return)
class ReturnAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'reason', 'return_date', 'status')
    search_fields = ('order__user__phone_number', 'product__name', 'reason')
    list_filter = ('return_date', 'status')

@admin.register(Exchange)
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('return_order', 'new_product', 'exchange_date')
    search_fields = ('return_order__order__user__phone_number', 'new_product__name')
    list_filter = ('exchange_date',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'subscription_type', 'start_date', 'end_date')
    search_fields = ('user__phone_number', 'subscription_type')
    list_filter = ('start_date', 'end_date')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'notification_date', 'is_read')
    search_fields = ('user__phone_number', 'message')
    list_filter = ('notification_date', 'is_read')
