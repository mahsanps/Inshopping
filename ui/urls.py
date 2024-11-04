from django.urls import path, include
from . import views
from .views import set_language
from ui.view.auth import SignInView, LogOutView, SignUpView, accountInfoView, EditAccountInfo
from ui.view.profile import ProfileView, AboutUs, ProductsSection, Contact
from ui.view.shop import CreateShop, EditShop
from ui.view.storepage import StorePage, aboutShop
from ui.view.products import ProductsView, PublishProductInstagramPost, CategoryAutocomplete, load_subcategories, ProductsListView, ProductDetails, EditProductView, DeleteProduct, SubcategoryProducts
from ui.view.category import CategoryPageView
from ui.view.productQuantity import ProductQuantityView, EditProductVariation
from ui.view.singleproductpage import SingleProductPage, AvailableColorsView
from ui.view.facebook_login import facebook_login
from ui.view.cart import CartView, CheckoutView, SuccessfulOrdr, OrderDetailView, OrderListView, UpdateCartItemView, DeleteCartItemView
from ui.view.search import Search_view
from ui.view.dashboard import Dashboard, ShopOrdersView, OrderDeliveryView, Reports
from ui.view.wallet import BankAccountView, WalletView, EditBankAccount
from ui.view.contact import contact_view
from ui.view.payment import zarinpal_callback, success_view, initiate_payment, callback_redirect
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('set-language/', set_language, name='set_language'),
    path("facebook-login/", facebook_login, name="facebook_login"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("signin/", SignInView.as_view(), name="signin"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path("account-info/", AboutUs.as_view(), name="account-info"),
    path('accountinfo/', accountInfoView.as_view(), name='accountinfo'),
    path("editaccountinfo/<int:pk>/", EditAccountInfo.as_view(), name='editaccountinfo'),
    path("contact/", Contact.as_view(), name="contact"),
    path("createshop/", CreateShop.as_view(), name="create_shop"),
    path("editshop/<int:pk>/", EditShop.as_view(), name='editshop'),
    path("products/", ProductsView.as_view(), name="products"),
    path("product/<str:product_pk>/publish-instagram-post/", PublishProductInstagramPost.as_view(), name="publish_product_instagram_post"),
    path("productssection/", ProductsSection.as_view(), name="productssection"),
    path("productslist/", ProductsListView.as_view(), name="products_list"),
    path("productimages/", ProductsView.as_view(), name="product_images"),
    path("logout/", LogOutView.as_view(), name="logout"),
    path("category/<slug:category_slug>/", CategoryPageView.as_view(), name="category"),
    path("subcategory/<slug:subcategory_slug>/", SubcategoryProducts.as_view(), name="subcategory"),
    path("productsquantity/<str:product_pk>/", ProductQuantityView.as_view(), name="products_quantity"),
    path("productdetails/<str:product_pk>/", ProductDetails.as_view(), name="product_details"),
    path("editproduct/<int:product_pk>/", EditProductView.as_view(), name="edit_product"),
    path("productedit/<int:product_pk>/", EditProductVariation.as_view(), name="product_edit"),
    path("producteditvariation/<int:product_pk>/", EditProductVariation.as_view(), name="product_editvariation"),
    path('deleteproduct/<product_pk>/', DeleteProduct.as_view(), name='delete_product'),
    path('searchresults', Search_view.as_view(), name='searchresults'),
    path('subcategory-autocomplete/', CategoryAutocomplete.as_view(), name='subcategory_autocomplete'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('orderdetails/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('successful_order', SuccessfulOrdr.as_view(), name='successful_order'),
    path('loadsubcategories/', load_subcategories, name='loadsubcategories'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('reports/', Reports.as_view(), name='reports'),
    path('order-registered-details/<int:pk>', ShopOrdersView.as_view(), name='order-registered-details'),
    path('bankaccount/', BankAccountView.as_view(), name='bankaccount'),
    path('editbankaccount/<int:pk>/', EditBankAccount.as_view(), name='editbankaccount'),
    path('wallet/', WalletView.as_view(), name='mywallet'),
    path('terms&conditions/', views.Terms_Conditions, name='terms&conditions'),
    path('privacy-policy/', views.Privacy_Policy, name='privacy_policy'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog, name='blog'),
    path('guid/', views.guid, name='guid'),
    path('contactus/', contact_view, name='contactus'),
    path('callback/<str:store_name>/', zarinpal_callback, name='zarinpal_callback'),  
    path('success/', success_view, name='success'),
    path('order-delivery/<int:order_id>/', OrderDeliveryView.as_view(), name='order_delivery'),
    
    
    path("", views.Index_view, name="index"),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    # Store-specific URLs
    path('<str:store_name>/', StorePage.as_view(), name='storepage'),
    path('<str:store_name>/aboutshop/', aboutShop.as_view(), name='about-shop'),
    path('<str:store_name>/cart/', CartView.as_view(), name='cart'),
    path('<str:store_name>/checkout/', CheckoutView.as_view(), name='checkout'),
    path('<str:store_name>/update_cart_item/<str:variation_pk>/', UpdateCartItemView.as_view(), name='update_cart_item'),
    path('<str:store_name>/delete_cart_item/<str:variation_pk>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
    path('<str:store_name>/availablecolor/<int:product_pk>/', AvailableColorsView.as_view(), name='available_colors'),
    path('<str:store_name>/<str:product_pk>/', SingleProductPage.as_view(), name='singleproductpage'),
    path('callback/<str:store_name>/', callback_redirect, name='callback_redirect'),
    path('initiate-payment/<int:order_id>/', initiate_payment, name='initiate_payment'),  # Add this line for payment initiation
]
