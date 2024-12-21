from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from django.conf import settings


class Command(BaseCommand):
    help = "Create or Update Site Record"

    def handle(self, *args, **options):
        site = Site.objects.filter(domain="example.com").first()
        created = False
        if site:
            site.domain = settings.SITE_URL
            site.name = settings.SITE_NAME
            site.save()
            created = True
        else:
            site, created = Site.objects.get_or_create(
                domain=settings.SITE_URL, name=settings.SITE_NAME
            )

        if created:
            self.stdout.write(self.style.SUCCESS("Successfully created site."))
        else:
            self.stdout.write(self.style.SUCCESS("Site already exists."))
