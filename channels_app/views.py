from django.http import HttpResponse
from .models import Channel, Post

  
def index(request):
    return HttpResponse(f'Hello Channels')
