from django import forms
from myapp.models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = ['date', 'trade_code', 'high', 'low', 'open', 'close', 'volume']
