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


@login_required
def instagram_login(request):
    """
    Redirects the user to Instagram's authorization page.
    """
    instagram_auth_url = 'https://api.instagram.com/oauth/authorize'
    redirect_uri = request.build_absolute_uri('/instagram/callback/')
    client_id = settings.INSTAGRAM_CLIENT_ID
    scope = 'user_profile,user_media'  # Add required scopes
    
    # Create the authorization URL
    auth_url = f"{instagram_auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=code"
    return redirect(auth_url)


@login_required
def instagram_callback(request):
    """
    Handles the callback from Instagram and obtains a long-lived access token.
    """
    code = request.GET.get('code')
    if not code:
        return render(request, 'store/error.html', {'message': 'Authorization failed or was denied by the user.'})

    # Step 3: Exchange the authorization code for a short-lived access token
    short_lived_token = exchange_code_for_short_lived_token(code)

    if short_lived_token:
        # Step 4: Exchange the short-lived token for a long-lived access token
        long_lived_token, expires_in = exchange_for_long_lived_token(short_lived_token)
        
        if long_lived_token:
            # Step 5: Store the token
            store_access_token(request.user, long_lived_token, expires_in)
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