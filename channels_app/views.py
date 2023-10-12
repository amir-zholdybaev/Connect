from django.http import HttpResponse
from .models import Channel, Post

  
def index(request):
    post = Post.objects.get(pk=1)
    return HttpResponse(f'<img src="{post.image.url}">')
