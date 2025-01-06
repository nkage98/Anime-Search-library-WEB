from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):
        if request.method == "POST":
                search = request.POST['search']
                url = f'https://api.jikan.moe/v4/anime?q={search}&limit=20'
                data = requests.get(url)
                animes = data.json().get("data")

                return render(request, 'home.html', {'animes':animes, 'search':search})

        else:
                url = "https://api.jikan.moe/v4/top/anime"
                data = requests.get(url)
                animes = data.json().get("data")

                return render(request, 'home.html', {'animes': animes})

        
def anime_info(request, anime_id):

        url = f'https://api.jikan.moe/v4/anime/{anime_id}'
        data = requests.get(url)
        animes = data.json().get("data")

        return render(request, 'anime_info.html', {'animes':animes})
                

        
    
    
    

