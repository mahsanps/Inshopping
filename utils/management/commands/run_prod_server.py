from django.core.management.base import BaseCommand
import os
import subprocess
import shlex
from django.conf import settings


class Command(BaseCommand):
    help = "Starts production server"

    def add_arguments(self, parser):
        parser.add_argument(
            "--concurrency",
            type=int,
            required=False,
            default=4,
        )

    def handle(self, *args, **options):
        concurrency = options["concurrency"]
        subprocess.run(
            shlex.split(
                f"uvicorn inshopping.asgi:application --host 0.0.0.0 --port 8000 --workers {concurrency}"
            ),
            check=True,
        )
