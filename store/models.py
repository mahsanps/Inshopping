from django.db import models
from utils.models import BaseModel
import uuid
import json
from django.core.serializers import serialize
from django.db.models.query import QuerySet
from django.db.models import Model
from authuser.models import Account
from .choices import OrderStatusChoices, ProductVariationTypeChoices
from django.contrib.auth import get_user_model
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import make_aware
import jdatetime

# Create your models here.

User = get_user_model()

class DjangoJSONEncoder(json.JSONEncoder):

    def default(self, obj):
        # Convert QuerySets to a list of dictionaries
        try:
            if isinstance(obj, QuerySet):
                return json.loads(serialize('json', obj))

            # Convert Model instances to dictionaries
            elif isinstance(obj, Model):
                return json.loads(serialize('json', [obj]))[0]
            return super(DjangoJSONEncoder, self).default(obj)
        except:
            try: 
                return str(obj)
            except:
                return ""

class AccountInfo(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account_info", verbose_name=_("user"))
    firstname= models.CharField(max_length=300, verbose_name=_("firstname"))
    lastname= models.CharField(max_length=300, verbose_name=_("lastname"))
    phone= models.CharField(max_length=300, verbose_name=_("phone"))
    

      
        
class Category(BaseModel):
    name=models.CharField(max_length=100, verbose_name=_("Category"))
    image=models.ImageField(upload_to='media/static/images/', null=True, blank=True) 
 
class SubCategory(BaseModel):
    subname=models.CharField(max_length=200, verbose_name=_("Subcategory"))
    categoryname=models.ForeignKey(Category, on_delete=models.CASCADE, default="") 
    image=models.ImageField(upload_to='media/static/images/', null=True, blank=True) 
    
    def __str__(self):
        return f'{self.subname}' 

class Shop(BaseModel):
    is_approved = models.BooleanField(default=False)
    store_name=models.CharField(max_length=400, verbose_name=_("Storename"))
    account=models.ForeignKey(User,on_delete=models.CASCADE,  verbose_name=_("account")) 
    description=models.TextField(blank=True,verbose_name=_("Description"))
    instagramId=models.CharField(max_length=400, verbose_name=_("InstagramId"))
    email=models.EmailField( verbose_name=_("Email"))
    contact=models.CharField(blank=True,max_length=20, verbose_name=_("Contact"))
    address=models.CharField(blank=True, max_length=400, verbose_name=_("Address"))
    image=models.ImageField(upload_to='media/static/images/', default="",  verbose_name=_("Image"))
    delivery_cost=models.IntegerField(default=0,verbose_name=_("delivery-cost"))
    banner_image1=models.ImageField(upload_to='media/static/images/', default="",  verbose_name=_("banner-Image1"))
    banner_image2=models.ImageField(upload_to='media/static/images/', default="",  verbose_name=_("banner-Image2"))
    banner_image3=models.ImageField(upload_to='media/static/images/', default="",  verbose_name=_("banner-Image3"))
    
    def __str__(self):
        return f'{self.store_name}' 
    
   
      
 
class Color(models.Model):
    color = models.CharField(max_length=400,default="", verbose_name=_("color"))
    def __str__(self):
        return f'{self.color}'



class Product(BaseModel):
    is_approved = models.BooleanField(default=False)
    name=models.CharField(max_length=200, default="",  verbose_name=_("productName"))
    productCode=models.CharField(blank=True, max_length=500,  verbose_name=_("productCode"))
    image=models.ImageField(upload_to='media/static/images/', default="",  verbose_name=_("Image"))
    description=models.TextField(default="",null=True, blank=True, verbose_name=_("Description"))
    material=models.CharField(max_length=200,null=True, blank=True,  verbose_name=_("material"))
    madeIn=models.CharField(max_length=200,null=True, blank=True,  verbose_name=_("madeIn"))
    price=models.IntegerField(default=0,  verbose_name=_("Price")) 
    isactive=models.BooleanField(default=True,  verbose_name=_("isactive"))
    category=models.ForeignKey(Category, on_delete=models.CASCADE,  verbose_name=_("Category"))
    subcategory=models.ForeignKey(SubCategory, on_delete=models.CASCADE, default="", verbose_name=_("subcategory"))
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True, verbose_name=_("shop"))
    
    

   
class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(upload_to='media/static/images/',  verbose_name=_("Images"))
    

class ProductVariation(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="variations")
    size = models.CharField(max_length=400, default="", null=True, blank=True,  verbose_name=_("size"))
    color = models.ForeignKey(Color, on_delete=models.CASCADE, null=True, blank=True,  verbose_name=_("color"))
    quantity = models.IntegerField(default=1,  verbose_name=_("quantity"))
    
    def __str__(self):
        return f'{self.size} {self.color} ({self.quantity})'



class BankAccount(BaseModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, null=True, blank=True)
    name= models.CharField(max_length=200, default="",  verbose_name=_("name"))
    bankName=models.CharField(max_length=200, default="",  verbose_name=_("bankName"))
    cartNumber=models.CharField(max_length=200, default="",  verbose_name=_("cartNumber"))
    accountNumber=models.CharField(max_length=200, default="",  verbose_name=_("accountNumber"))
    





class Order(BaseModel):
    created_at = jmodels.jDateTimeField()
    account = models.ForeignKey(Account, on_delete=models.DO_NOTHING, db_constraint=False, null=False, blank=True,  verbose_name=_("account"))
    is_paid = models.BooleanField(default=False)
    total_price = models.FloatField( verbose_name=_("totalPrice"))
    total_discount = models.FloatField( verbose_name=_("totalDiscount"))
    delivery_address_unit_number = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("unitNumber"))
    delivery_address_street_name = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("streetName"))
    delivery_address_suburb = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("suburb"))
    delivery_address_city = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("city"))
    delivery_address_state = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("state"))
    delivery_address_country = models.CharField(max_length=200, blank=True, null=True)
    delivery_address_postcode = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("postCode"))
    mobile_number = models.CharField(max_length=200, blank=True, null=True,  verbose_name=_("mobileNumber"))
    email = models.EmailField(blank=True, null=True)
    payment_authority = models.CharField(max_length=50, blank=True, null=True)
    payment_status = models.BooleanField(default=False)
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE,  db_constraint=False, null=False, blank=False, verbose_name=_("shop"))
    
    def save(self, *args, **kwargs):
        # Manually set `created_at` with a timezone-aware Jalali datetime if it's not set
        if not self.created_at:
            # Get current Jalali date and convert to Gregorian
            jalali_now = jdatetime.datetime.now()
            gregorian_now = jalali_now.togregorian()
            
            # Convert it to a timezone-aware datetime
            self.created_at = make_aware(gregorian_now)
        
        # Check if the order is being marked as paid
        if self.pk:
            try:
                old_order = Order.objects.get(pk=self.pk)
                if not old_order.is_paid and self.is_paid:
                    # If the order was not paid before but is now being marked as paid
                    if hasattr(self, 'items'):
                        for item in self.items.all():
                            if item.variation:
                                new_quantity = item.variation.quantity - item.quantity
                                item.variation.quantity = max(new_quantity, 0)  # Ensure quantity doesn't go below zero
                                item.variation.save(update_fields=["quantity"])
            except Order.DoesNotExist:
                pass  # Handle error if needed

        super().save(*args, **kwargs)

    
    
    def full_delivery_address(self):
        address_parts = [
            self.delivery_address_unit_number,
            self.delivery_address_street_name,
            self.delivery_address_suburb,
            self.delivery_address_city,
            self.delivery_address_state,
        ]
        return ", ".join(part for part in address_parts if part)
    



class OrderItem(BaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items")
    variation = models.ForeignKey(ProductVariation, on_delete=models.DO_NOTHING, db_constraint=False, null=True, blank=True, related_name="order_items")
    total_price = models.FloatField( verbose_name=_("totalPrice"))
    variation_price = models.FloatField()
    discount = models.FloatField( verbose_name=_("discount"))
    quantity=models.IntegerField(default=1,  verbose_name=_("quantity"))
    
    def save(self, *args, **kwargs):
        # Check if there is a variation and if the variation has enough quantity
        if self.variation and self.variation.quantity - self.quantity < 0:
            raise Exception("There is not enough item available to submit this order")

        # Call the original save method to save the order item first
        super().save(*args, **kwargs)
    
class OrderDelivery(BaseModel):
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="delivery")
    status = models.CharField(max_length=200, choices=OrderStatusChoices.choices, default='registered',  verbose_name=_("status"))
    tracking_number = models.CharField(max_length=250, null=True, blank=True,  verbose_name=_("trackingNumber"))
    


class Contact(BaseModel):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=400)
    email = models.EmailField(max_length=1000)
    message = models.CharField(max_length=3000)
         
    
