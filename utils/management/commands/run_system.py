from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
import os


class Command(BaseCommand):
    help = "Set up the project with initial data"

    def handle(self, *args, **options):
        self.stdout.write("Starting project setup...")

        self.stdout.write("Setup project...")
        call_command("setup_project")
        self.stdout.write(self.style.SUCCESS("Setup project completed..."))

        self.stdout.write("Starting production server...")
        call_command("run_prod_server")
