
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import Trade
from myapp.forms import TradeForm

def home(request):
    trades = Trade.objects.all()
    return render(request, 'myapp/home.html', {'trades': trades})

def add_trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TradeForm()
    return render(request, 'myapp/add_trade.html', {'form': form})
def update_trade(request, pk):
    trade = get_object_or_404(Trade, pk=pk)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TradeForm(instance=trade)
    return render(request, 'myapp/update_trade.html', {'form': form})

def delete_trade(request, pk):
    trade = get_object_or_404(Trade, pk=pk)
    if request.method == 'POST':
        trade.delete()
        return redirect('home')
    return render(request, 'myapp/delete_trade.html', {'trade': trade})


 

from django.shortcuts import render

def trades(request):
    # Fetch data from your database or any other source
    dates = [...]  # List of sorted dates
    close_prices = [...]  # List of close prices
    volumes = [...]  # List of volumes
    trade_codes = [...]  # List of trade codes

    return render(request, 'trades.html', {
        'dates': dates,
        'close_prices': close_prices,
        'volumes': volumes,
        'trade_codes': trade_codes,
    })
# views.py

 
import json

def visualize_data(request):
    with open('D:\\myproject\\trades.json..json', 'r') as file:
        data = json.load(file)
    
    return render(request, 'myapp/trade.html', {'data': data})
def contact(request):
    return render(request, 'myapp/aboutdevloper.html')

def about_project(request):
    return render(request, 'myapp/about.html')