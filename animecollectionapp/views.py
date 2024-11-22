from django.shortcuts import render
from django.http import HttpResponse
import requests

def home(request):

    url = "https://api.jikan.moe/v4/top/anime?filter=bypopularity"

    try:
        response = requests.get(url)
        topanimes = response.json().get("data")
        topanimestitle = []
        for i, data in enumerate(topanimes):
            topanimestitle.append(data["title"])
        return render(request, 'home.html', {'topanimes':topanimestitle})
    
    except:
        return response.status_code
    
    #topanimesthumb = []
    #topanimestitle= topanimes['data'][0]['title']
    
        #topanimesthumb.append(data['images']['jpg']['image_url'])
    
    #print(topanimesthumb[0])
    

