import json
from datetime import datetime
from django.core.management.base import BaseCommand
from myapp.models import Trade

class Command(BaseCommand):
    help = 'Load trades data from JSON file'

    def handle(self, *args, **kwargs):
        with open('D:\\myproject\\trades.json..json', 'r') as file:
            trades = json.load(file)
            for trade in trades:
                Trade.objects.create(
                    date=datetime.strptime(trade['date'], '%Y-%m-%d'),
                    trade_code=trade['trade_code'],
                    high=float(trade['high'].replace(',', '')),  # Remove commas
                    low=float(trade['low'].replace(',', '')),    # Remove commas
                    open=float(trade['open'].replace(',', '')),  # Remove commas
                    close=float(trade['close'].replace(',', '')),# Remove commas
                    volume=int(trade['volume'].replace(',', ''))
                )
        self.stdout.write(self.style.SUCCESS('Trades data loaded successfully'))
