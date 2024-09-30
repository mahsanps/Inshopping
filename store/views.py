import requests
from django.shortcuts import redirect, render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import HttpResponse
from .utils import (
    exchange_code_for_short_lived_token,
    exchange_for_long_lived_token,
    store_access_token,
)
from urllib.parse import urlencode
from authuser.models import Account
from django.urls import reverse

@login_required
def instagram_login(request):
    """
    Redirects the user to Instagram's authorization page.
    """
    
    
    
    
    instagram_auth_url = 'https://www.instagram.com/oauth/authorize'
    redirect_uri = request.build_absolute_uri(reverse("instagram_callback"))
    client_id = settings.INSTAGRAM_CLIENT_ID
    scope = 'instagram_business_basic,instagram_business_content_publish,instagram_business_manage_messages,instagram_business_manage_comments'
    scope = "%2C".join(scope.split(","))
    # Add the user ID or another identifier to the redirect URI as a query parameter
    redirect_uri_with_params = f"{redirect_uri}"
    # Create the authorization URL
    auth_url = f"{instagram_auth_url}?enable_fb_login=0&force_authentication=1&client_id={client_id}&redirect_uri={redirect_uri_with_params}&scope={scope}&response_type=code"
    
    
    return redirect(auth_url)



def instagram_callback(request):
    """
    Handles the callback from Instagram and obtains a long-lived access token.
    """
    # Get the user_id that was passed in the redirect URI
    user_id = request.user.id
    # Ensure the user exists
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        return render(request, 'store/instagram_error.html', {'message': 'Invalid user ID.'})

    # Get the authorization code from the request
    code = request.GET.get('code')
    if not code:
        return render(request, 'store/instagram_error.html', {'message': 'Authorization failed or was denied by the user.'})


    # Exchange the authorization code for a short-lived access token
    short_lived_token = exchange_code_for_short_lived_token(request, code)

    if short_lived_token:
        # Exchange the short-lived token for a long-lived access token
        long_lived_token, expires_in = exchange_for_long_lived_token(short_lived_token)
        
        if long_lived_token:
            # Store the token, associating it with the user retrieved from the user_id
            store_access_token(user, long_lived_token, expires_in)
            return render(request, 'store/instagram_success.html', {'message': 'Instagram account successfully connected!'})
        else:
            return render(request, 'store/instagram_error.html', {'message': 'Failed to obtain a long-lived token.'})
    else:
        return render(request, 'store/instagram_error.html', {'message': 'Failed to obtain a short-lived token.'})

@login_required
def instagram_success(request):
    return render(request, 'instagram_success.html', {'message': 'Instagram account successfully connected!'})

# Optional: Error view to show in case of authentication failure
@login_required
def instagram_error(request):
    return render(request, 'instagram_error.html', {'message': 'There was an error connecting your Instagram account.'})



