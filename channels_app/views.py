from django.http import HttpResponse
from .models import Channel

  
def index(request):
    channel = Channel.objects.get(pk=1)

    return HttpResponse(f'Hello {channel.name}')
