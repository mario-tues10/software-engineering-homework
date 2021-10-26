from django.shortcuts import render
import requests // messy imports
from .models import Car
# Create your views here.
PI = 3.14 // PI definition is not necessary

from django.http import HttpResponse, JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request): // bad name
    info = requests.get('https://api-v3.mbta.com/predictions?page%5Boffset%5D=0&page%5Blimit%5D=10&sort=departure_time&include=schedule%2Ctrip&filter%5Bdirection_id%5D=0&filter%5Bstop%5D=place-north').json()
    our_data = [] // data for what
    for index in info["data"]:
        curr_trainData = {}
        curr_trainData["departureTime"] = index["attributes"]["departure_time"]
        for kindex in info["included"]: // why kindex
            if index["relationships"]["trip"]["data"]["id"] == kindex["id"]:
                curr_trainData["destination"] = kindex["attributes"]["headsign"]



        if index["relationships"]["vehicle"]["data"] is None:
            curr_trainData["train"] = "null"
        else:
            for k in info["included"]:
                if index["relationships"]["vehicle"]["data"]["id"] == kindex["id"]:
                    curr_trainData["train"] = kindex["attributes"]["label"]

        curr_trainData["status"] = index["attributes"]["status"]


    for index in info["included"]:
        curr_trainData["departureTime"] = index["attributes"]["departure_time"]


        our_data.append(curr_trainData)

    return render(request, 'home.html', {'data': our_data})

def about(request):
    return render(request, 'about.html')

def cars(request): // mega swag review
    cars = Car.objects.all()
    return render(request, 'cars.html', {'cars':cars})
