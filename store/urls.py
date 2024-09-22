from django.urls import path
from . import views

urlpatterns = [
    # URL to initiate the Instagram login and authorization process
    path('instagram/login/', views.instagram_login, name='instagram_login'),

    # URL to handle the callback from Instagram after user authorization
    path('instagram/callback/', views.instagram_callback, name='instagram_callback'),

    # Optional: Success page to show when Instagram account is successfully connected
    path('instagram/success/', views.instagram_success, name='instagram_success'),

    # Optional: Error page to show in case of authentication failure
    path('instagram/error/', views.instagram_error, name='instagram_error'),
]
