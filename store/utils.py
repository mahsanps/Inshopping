import requests
from django.conf import settings
from django.utils.timezone import now, timedelta
from .models import ShopAuth

def exchange_code_for_short_lived_token(code):
    """
    Exchanges the authorization code for a short-lived access token.
    """
    url = 'https://api.instagram.com/oauth/access_token'
    redirect_uri = settings.INSTAGRAM_REDIRECT_URI
    client_id = settings.INSTAGRAM_CLIENT_ID
    client_secret = settings.INSTAGRAM_CLIENT_SECRET

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri,
        'code': code
    }

    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        return None

def exchange_for_long_lived_token(short_lived_token):
    """
    Exchanges a short-lived token for a long-lived access token.
    """
    url = 'https://graph.instagram.com/access_token'
    params = {
        'grant_type': 'ig_exchange_token',
        'client_secret': settings.INSTAGRAM_CLIENT_SECRET,
        'access_token': short_lived_token
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('access_token'), data.get('expires_in')
    else:
        return None, None

def store_access_token(user, access_token, expires_in):
    """
    Stores the access token in the database.
    """
    instagram_user_id = get_instagram_user_id(access_token)  # Fetch Instagram User ID using the access token
    if instagram_user_id:
        expiry_date = now() + timedelta(seconds=expires_in)
        ShopAuth.objects.update_or_create(
            user=user,
            defaults={
                'instagram_user_id': instagram_user_id,
                'access_token': access_token,
                'token_expiry': expiry_date,
                'last_authenticated': now()
            }
        )

def get_instagram_user_id(access_token):
    """
    Fetches the Instagram User ID using the access token.
    """
    url = 'https://graph.instagram.com/me'
    params = {
        'fields': 'id,username',
        'access_token': access_token
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json().get('id')
    else:
        return None
