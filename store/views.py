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

@login_required
def instagram_login(request):
    """
    Redirects the user to Instagram's authorization page.
    """
    instagram_auth_url = 'https://api.instagram.com/oauth/authorize'
    redirect_uri = request.build_absolute_uri('/instagram/callback/')
    client_id = settings.INSTAGRAM_CLIENT_ID
    scope = 'user_profile,user_media'  # Add required scopes
    
    # Add the user ID or another identifier to the redirect URI as a query parameter
    query_params = urlencode({'user_id': request.user.id})
    redirect_uri_with_params = f"{redirect_uri}?{query_params}"
    
    # Create the authorization URL
    auth_url = f"{instagram_auth_url}?client_id={client_id}&redirect_uri={redirect_uri_with_params}&scope={scope}&response_type=code"
    return redirect(auth_url)


def instagram_callback(request):
    """
    Handles the callback from Instagram and obtains a long-lived access token.
    """
    # Get the user_id that was passed in the redirect URI
    user_id = request.GET.get('user_id')
    
    # Ensure the user exists
    try:
        user = Account.objects.get(id=user_id)
    except Account.DoesNotExist:
        return render(request, 'store/error.html', {'message': 'Invalid user ID.'})

    # Get the authorization code from the request
    code = request.GET.get('code')
    if not code:
        return render(request, 'store/error.html', {'message': 'Authorization failed or was denied by the user.'})

    # Exchange the authorization code for a short-lived access token
    short_lived_token = exchange_code_for_short_lived_token(code)

    if short_lived_token:
        # Exchange the short-lived token for a long-lived access token
        long_lived_token, expires_in = exchange_for_long_lived_token(short_lived_token)
        
        if long_lived_token:
            # Store the token, associating it with the user retrieved from the user_id
            store_access_token(user, long_lived_token, expires_in)
            return render(request, 'store/success.html', {'message': 'Instagram account successfully connected!'})
        else:
            return render(request, 'store/error.html', {'message': 'Failed to obtain a long-lived token.'})
    else:
        return render(request, 'store/error.html', {'message': 'Failed to obtain a short-lived token.'})

@login_required
def instagram_success(request):
    return render(request, 'success.html', {'message': 'Instagram account successfully connected!'})

# Optional: Error view to show in case of authentication failure
@login_required
def instagram_error(request):
    return render(request, 'error.html', {'message': 'There was an error connecting your Instagram account.'})