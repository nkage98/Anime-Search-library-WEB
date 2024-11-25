from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
        if request.method == "GET":
                    search = request.GET['search']
                    url = f'https://api.jikan.moe/v4/anime?q={search}&limit=20'
                    data = requests.get(url)
                    animes = {}
                    animes['animes_data'] = data.json().get("data")

                    return render(request, 'home.html', animes)

        
        else:
                url = "https://api.jikan.moe/v4/top/anime"
                data = requests.get(url)
                animes = {}
                animes['animes_data'] = data.json().get("data")

                return render(request, 'home.html', animes)

        

    
    
    

