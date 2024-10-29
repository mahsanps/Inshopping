from store.models import Shop
from django.shortcuts import render, redirect
from django import forms

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('store_name', 'description', 'instagramId', 'email', 'contact', 'address','delivery_cost','image', 'banner_image1','banner_image2','banner_image3')

    def __init__(self, *args, **kwargs):
        super(ShopForm, self).__init__(*args, **kwargs)
        self.fields['store_name'].required = True
        self.fields['description'].required = False
        self.fields['instagramId'].required = True
        self.fields['email'].required = True
        self.fields['contact'].required = True
        self.fields['address'].required = False
        self.fields['delivery_cost'].required = True
        self.fields['image'].required = True
        self.fields['banner_image1'].required = True
        self.fields['banner_image2'].required = True
        self.fields['banner_image3'].required = True
        
     
        self.fields['store_name'].widget.attrs.update({
            'placeholder': 'name',
            
        })
        self.fields['delivery_cost'].help_text = '(هزینه ارسال کالا یکبار برای تمام محصولات شما اعمال می شود.(هزینه به تومان))'
        self.fields['store_name'].help_text =  '(نام فروشگاه شما به عنوان وبسایت شما معرفی می شود و حتما باید با حروف لاتین نوشته شود. در صورتی که نام فروشگاه شما بیش از یک کلمه است بین کلمات فاصله گذاشته نشود و از (-) استفاده شود. مثال : parvane-shop)'
        self.fields['image'].label = "لوگوی فروشگاه"