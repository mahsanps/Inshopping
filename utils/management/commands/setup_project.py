from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = "Set up the project with initial data"

    def handle(self, *args, **options):
        self.stdout.write("Starting project setup...")

        self.stdout.write("Running migrate...")
        call_command("migrate")
        self.stdout.write(self.style.SUCCESS("migration completed..."))

        self.stdout.write("Creating site ...")
        call_command("create_site")
        self.stdout.write(self.style.SUCCESS("Creating site completed..."))

        self.stdout.write("Collecting static...")
        call_command("collectstatic", "--noinput")
        self.stdout.write(self.style.SUCCESS("Collecting static completed..."))

        self.stdout.write("Creating admin account...")
        call_command("create_admin_account")
        self.stdout.write(self.style.SUCCESS("Creating admin account completed..."))

        self.stdout.write(self.style.SUCCESS("Project setup complete."))
