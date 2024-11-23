from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
    try:
        url = "https://api.jikan.moe/v4/top/anime?filter=bypopularity"
    except:
        return response.status_code
    
    response = requests.get(url)
    topanimes = {}
    topanimes['animes_data'] = response.json().get("data")

    return render(request, 'home.html', topanimes)

    
    
    
    

