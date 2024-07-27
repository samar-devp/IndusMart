from django import forms
from .models import (
    User, Role, UserRole, Category, Product, ProductAttribute, Order, 
    OrderDetail, Cart, CartItem, Payment, Supplier, Inventory, Review, 
    Wishlist, WishlistItem, Discount, OrderDiscount, AuditLog, Return, 
    Exchange, Subscription, Notification, OTP
)

# EMAIL OTP
class OTPForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ['email']

class OTPValidationForm(forms.ModelForm):
    class Meta:
        model = OTP
        fields = ['email', 'otp']

# User form
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

# Role form
class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = '__all__'

# UserRole form
class UserRoleForm(forms.ModelForm):
    class Meta:
        model = UserRole
        fields = '__all__'

# Category form
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

# Product form
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

# ProductAttribute form
class ProductAttributeForm(forms.ModelForm):
    class Meta:
        model = ProductAttribute
        fields = '__all__'

# Order form
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

# OrderDetail form
class OrderDetailForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields = '__all__'

# Cart form
class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = '__all__'

# CartItem form
class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = '__all__'

# Payment form
class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'

# Supplier form
class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

# Inventory form
class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'

# Review form
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

# Wishlist form
class WishlistForm(forms.ModelForm):
    class Meta:
        model = Wishlist
        fields = '__all__'

# WishlistItem form
class WishlistItemForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = '__all__'

# Discount form
class DiscountForm(forms.ModelForm):
    class Meta:
        model = Discount
        fields = '__all__'

# OrderDiscount form
class OrderDiscountForm(forms.ModelForm):
    class Meta:
        model = OrderDiscount
        fields = '__all__'

# AuditLog form
class AuditLogForm(forms.ModelForm):
    class Meta:
        model = AuditLog
        fields = '__all__'

# Return form
class ReturnForm(forms.ModelForm):
    class Meta:
        model = Return
        fields = '__all__'

# Exchange form
class ExchangeForm(forms.ModelForm):
    class Meta:
        model = Exchange
        fields = '__all__'

# Subscription form
class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = '__all__'

# Notification form
class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'