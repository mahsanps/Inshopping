import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings
from ui.forms.contact import ContactForm

logger = logging.getLogger(__name__)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            
            try:
                form.save()
                # Clear the form after successful save
                form = ContactForm()  # Create a new empty form instance
                return JsonResponse({'success': True})
            except Exception as e:
                logger.error(f"Error saving contact form data: {e}")
                return JsonResponse({'success': False, 'error': str(e)}, status=500)
        else:
            logger.error(f"Form is invalid: {form.errors}")
            return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    
    return render(request, 'contactus.html', {'form': form})