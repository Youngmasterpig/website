from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template("")
    return HttpResponse("")


def details(request, album_id):
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")

