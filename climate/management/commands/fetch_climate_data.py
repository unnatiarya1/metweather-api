# climate/management/commands/fetch_climate_data.py

import requests
import pandas as pd
from django.core.management.base import BaseCommand
from climate.models import ClimateData

DATA_URL = 'https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/Tmax/date/UK.txt'

class Command(BaseCommand):
    help = "Fetch and parse UK Met Office climate data"

    def handle(self, *args, **kwargs):
        response = requests.get(DATA_URL)
        text = response.text

        lines = text.splitlines()
        data_lines = [line for line in lines if line and line[0].isdigit()]
        rows = []

        for line in data_lines:
            year = int(line[:4])
            monthly_values = line[5:].split()
            if len(monthly_values) >= 12:
                for month, value in enumerate(monthly_values[:12], start=1):
                    if value != "---":
                        rows.append((year, month, float(value)))

        for year, month, value in rows:
            ClimateData.objects.update_or_create(
                year=year,
                month=month,
                parameter='Tmax',
                region='UK',
                defaults={'value': value}
            )
        self.stdout.write(self.style.SUCCESS("✅ Climate data parsed and saved."))
