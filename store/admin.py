from django.contrib import admin
from .models import Shop, Category, Product, BankAccount, Order, Contact, SubCategory, ProductVariation, Color, ProductImage, OrderItem, OrderDelivery
from ui.forms.productQuantity import ProductsQuantityForm

# Inline for ProductImage
class ProductImageInlineAdmin(admin.StackedInline):
    model = ProductImage
    extra = 0

# Inline for ProductVariation
class ProductVariationInlineAdmin(admin.StackedInline):
    model = ProductVariation
    form = ProductsQuantityForm
    extra = 0

# Inline for Product
class ProductInlineAdmin(admin.StackedInline):
    model = Product
    extra = 0

# Inline for BankAccount in Shop
class ProductBankAccountAdmin(admin.StackedInline):
    model = BankAccount
    extra = 0

# Admin for Product
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        'description',
        'image',
        'material',
        'madeIn',
        'price',
        'isactive',
        'category',
        'productCode'
    ]
    inlines = [ProductVariationInlineAdmin, ProductImageInlineAdmin]

# Admin for Shop
class ShopAdmin(admin.ModelAdmin):
    list_display = [
        'store_name',
        'account',
        'description',
        'instagramId',
        'email',
        'address',
        'contact'
    ]
    inlines = [ProductBankAccountAdmin, ProductInlineAdmin]
    
    
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0
    
class OrderDeliveryInline(admin.TabularInline):
    model = OrderDelivery
    extra = 0
        
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline, OrderDeliveryInline]
    

# Register models with the admin site
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(SubCategory)
admin.site.register(ProductVariation)
admin.site.register(ProductImage)
admin.site.register(Color)
admin.site.register(BankAccount)
admin.site.register(Contact)

