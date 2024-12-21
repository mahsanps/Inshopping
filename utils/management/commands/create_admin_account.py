from django.conf import settings
from django.core.management.base import BaseCommand

from authuser.models import Account
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = "Create superuser"

    def handle(self, *args, **options):
        account, created = Account.objects.update_or_create(
            username=settings.ADMIN_USERNAME,
            defaults={
                "email": settings.ADMIN_EMAIL,
                "password": settings.ADMIN_PASSWORD,
                "is_staff": True,
                "is_superuser": True,
                "is_active": True,
            },
        )
        account.set_password(settings.ADMIN_PASSWORD)
        account.save()
        if created:
            self.stdout.write(self.style.SUCCESS("Admin user has created"))
        else:
            self.stdout.write(
                self.style.SUCCESS("Admin user already exists, it has been updated")
            )
