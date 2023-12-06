from django.shortcuts import render
from    posts.models import Post
def blog(request):
    data = Post.objects.all()
    return render(request, 'home.html', {'data':data}
    )