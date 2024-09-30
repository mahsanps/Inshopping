import requests
from django.conf import settings
from django.utils.timezone import now, timedelta

from django.urls import reverse
from urllib.parse import urlencode

def exchange_code_for_short_lived_token(request, code):
    """
    Exchanges the authorization code for a short-lived access token.
    """
    url = 'https://api.instagram.com/oauth/access_token'
    redirect_uri = request.build_absolute_uri(reverse("instagram_callback"))
    redirect_uri_with_params = f"{redirect_uri}"
    client_id = settings.INSTAGRAM_CLIENT_ID
    client_secret = settings.INSTAGRAM_CLIENT_SECRET

    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'authorization_code',
        'redirect_uri': redirect_uri_with_params,
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
        "access_token": short_lived_token
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
    from .models import ShopAuth
    if not expires_in:
        expires_in = 3600 * 24 * 365
    instagram_user_id = get_instagram_user_id(access_token)  # Fetch Instagram User ID using the access token
    if instagram_user_id:
        expiry_date = now() + timedelta(seconds=expires_in)
        shop = user.shop_set.first()
        ShopAuth.objects.update_or_create(
            shop=shop,
            defaults={
                'instagram_user_id': instagram_user_id,
                'access_token': access_token,
                'token_expiry': expiry_date,
                'last_authenticated': now()
            }
        )
        shop.instagramId = instagram_user_id
        shop.save()

def get_instagram_user_id(access_token):
    url = 'https://graph.instagram.com/v20.0/me'
    params = {
        'access_token': access_token,
        "fields": "user_id",
    }
    
    response = requests.get(url, params=params)
    print(55555, response.content)
    
    if response.status_code == 200:
        print(1111, response.json())
        data = response.json()
        return data.get("user_id")
        
    return None




def create_instagram_media(ig_user_id, image_url, caption, access_token):
    """
    Creates an Instagram media object (image or video).
    """
    url = f"https://graph.instagram.com/v20.0/{ig_user_id}/media"
    data = {
        'image_url': image_url,
        'caption': caption,
        'access_token': access_token
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json().get('id')  # Media object ID
    else:
        msg = (f"Error creating media: {response.status_code} - {response.text}")
        raise Exception(msg)
    
    
    
def publish_instagram_media(ig_user_id, creation_id, access_token):
    """
    Publishes the media object to the Instagram feed and returns the post ID.
    """
    url = f"https://graph.instagram.com/v20.0/{ig_user_id}/media_publish"
    data = {
        'creation_id': creation_id,
        'access_token': access_token
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        # Return the post ID from the response
        return response.json().get('id')  # This is the Instagram post ID
    else:
        msg = (f"Error publishing media: {response.status_code} - {response.text}")
        raise Exception(msg)




def post_to_instagram(ig_user_id, image_url, caption, access_token):
    """
    Creates and publishes a post on Instagram. Returns the Instagram post ID on success.
    """
    # Step 1: Create media object
    media_id = create_instagram_media(ig_user_id, image_url, caption, access_token)
    
    if media_id:
        # Step 2: Publish media object and get post ID
        post_id = publish_instagram_media(ig_user_id, media_id, access_token)
        if post_id:
            print("Post successfully published! Post ID:", post_id)
            return post_id  # Return the Instagram post ID
        else:
            print("Failed to publish post.")
            return None
    else:
        print("Failed to create media.")
        return None
