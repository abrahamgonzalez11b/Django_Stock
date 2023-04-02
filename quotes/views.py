from django.shortcuts import render

def home(request):
    import requests
    import json

    # pk_fdfe4d366e0b4b74b0d78eca8535435f
    api_request = requests.get('https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_fdfe4d366e0b4b74b0d78eca8535435f')

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = 'Error, Something went wrong...'

    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html', {})
