from django.shortcuts import render
from django.http import HttpResponse
from .model import Photo
from django.shortcuts import render
from django.http import Http404
# Create your views here.
def index(request):
    all_photos = Photo.object.all()
    template = loader.get_template('photoapp/index.html')
    context = {
        'all_photos' : all_photos
    }
    return render(request, 'photoapp.index.html', context)

def detail(request, photo_id):
    try:
        photo = Photo.objects.get(id==photo_id)
    except Photo.DoesNotExists:
        raise Http404('Photo not found')
    return render(request,'photoapp/detail.html',{'photo':photo})









