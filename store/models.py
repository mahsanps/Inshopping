from __future__ import annotations
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
from store.utils import post_to_instagram
from django.conf import settings
from django.utils.text import slugify
from unidecode import unidecode  # To handle Persian characters
from django.utils.timezone import is_aware, make_naive
from django.db import connection
from django.utils import timezone
from decouple import config, Csv
from django_jalali.db import models as jmodels
from datetime import timezone as dt_timezone



IS_LOCAL = config("IS_LOCAL", default=False, cast=bool)




from django.utils.timezone import now, timedelta
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
    

        
class Category(models.Model):
    name=models.CharField(max_length=100, verbose_name=_("Category"))
    image=models.ImageField(upload_to='media/static/images/', null=True, blank=True) 
    slug = models.SlugField(max_length=100, blank=True)  # Slug field


    def save(self, *args, **kwargs):
        # Generate the slug automatically from the name if slug is not provided
        if not self.slug:
            self.slug = slugify(unidecode(self.name))  # Converts Persian to ASCII-like slugs
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    

 
class SubCategory(BaseModel):
    subname=models.CharField(max_length=200, verbose_name=_("Subcategory"))
    categoryname=models.ForeignKey(Category, on_delete=models.CASCADE, default="") 
    image=models.ImageField(upload_to='media/static/images/', null=True, blank=True) 
    slug = models.SlugField(max_length=100, blank=True)  # Slug field


    def save(self, *args, **kwargs):
        # Generate the slug automatically from the name if slug is not provided
        if not self.slug:
            self.slug = slugify(unidecode(self.subname))  # Converts Persian to ASCII-like slugs
        super().save(*args, **kwargs)

    
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
   
    
    shop_auth: ShopAuth
    
    def __str__(self):
        return f'{self.store_name}' 
    
class ShopAuth(BaseModel):
    shop = models.OneToOneField(Shop, on_delete=models.CASCADE, related_name="shop_auth")
    # Instagram User ID
    instagram_user_id = models.CharField(max_length=255, unique=True)
    
    # Access token for making API requests on behalf of the user
    access_token = models.TextField()
    
    # Expiry date of the access token
    token_expiry = models.DateTimeField()  # Adjust if you know the exact expiry period
    
    # Date when the user last authenticated/authorized the app
    last_authenticated = models.DateTimeField(auto_now=True)
    
    # Optional fields for other metadata
    username = models.CharField(max_length=255, blank=True, null=True)
    profile_picture_url = models.URLField(blank=True, null=True)
    
    def is_token_valid(self):
        """
        Check if the access token is still valid.
        """
        return now() < self.token_expiry

    def __str__(self):
        return f'Instagram Account of {self.shop.account.username} (ID: {self.instagram_user_id})'      
 
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
    instagram_post_id = models.CharField(max_length=250, null=True, blank=True)
   
    
    def publish_to_instagram(self):
        instagram_user_id = self.shop.shop_auth.instagram_user_id
        access_token = self.shop.shop_auth.access_token
        caption = self.description
        image_url = self.image.url if not settings.IS_LOCAL else "https://th.bing.com/th?id=OIP.eKE8nrMRCK3bdvd62kWJ_wHaEK&w=333&h=187&c=8&rs=1&qlt=90&o=6&pid=3.1&rm=2"
        instagram_post_id = post_to_instagram(instagram_user_id, image_url, caption, access_token)
        self.instagram_post_id = instagram_post_id
        self.save()
        
   
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
    created_at = models.DateTimeField(auto_now_add=True)  
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
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, db_constraint=False, verbose_name=_("shop"))


    def save(self, *args, **kwargs):
        # Keep it in Gregorian, and handle timezone correctly
        if timezone.is_aware(self.created_at):
            self.created_at = self.created_at.astimezone(dt_timezone.utc).replace(tzinfo=None)
        super().save(*args, **kwargs)

    def get_jalali_created_at(self):
        # Convert Gregorian to Jalali for display
        return jdatetime.datetime.fromgregorian(datetime=self.created_at)
    
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
        if self.variation:
            if self.variation.quantity < self.quantity:
                raise Exception(f"Not enough items available. Only {self.variation.quantity} left in stock.")
            
            # Decrease the variation quantity by the order quantity
            self.variation.quantity -= self.quantity
            self.variation.save(update_fields=["quantity"])
        
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
         
    
